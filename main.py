from datetime import date
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from pwdlib import PasswordHash

from database import criar_tabelas, conectar_banco


app = FastAPI()

criar_tabelas()

password_hash = PasswordHash.recommended()

PERFIS_VALIDOS = [
    "administrador",
    "funcionario",
    "solicitante"
]


# Estrutura para cadastrar pedidos
class PedidoCriar(BaseModel):
    solicitante: str
    ferramenta_id: int
    prazo: str
    descricao: str = ""


# Estrutura para atualizar pedidos
class PedidoAtualizar(BaseModel):
    status: str
    feedback: str = ""


# Estrutura para cadastrar usuarios
class UsuarioCriar(BaseModel):
    nome: str = Field(min_length=1)
    email: EmailStr
    senha: str = Field(min_length=8)
    perfil: str = "solicitante"


# Estrutura para atualizar usuarios
class UsuarioAtualizar(BaseModel):
    nome: str = Field(min_length=1)
    email: EmailStr
    perfil: str


# Página inicial da API
@app.get("/")
def inicio():
    return {"mensagem": "Backend da Ferramentaria funcionando!"}


# Listar ferramentas
@app.get("/ferramentas")
def listar_ferramentas():
    conexao = conectar_banco()

    try:
        ferramentas = conexao.execute(
            "SELECT id, nome FROM ferramentas ORDER BY id"
        ).fetchall()

        return [dict(ferramenta) for ferramenta in ferramentas]
    finally:
        conexao.close()


# Listar pedidos ativos
@app.get("/pedidos")
def listar_pedidos():
    conexao = conectar_banco()

    try:
        pedidos = conexao.execute(
            "SELECT * FROM pedidos WHERE excluido = 0 ORDER BY id"
        ).fetchall()

        return [dict(pedido) for pedido in pedidos]
    finally:
        conexao.close()


# Cadastrar pedido
@app.post("/pedidos", status_code=201)
def criar_pedido(pedido: PedidoCriar):
    conexao = conectar_banco()

    try:
        ferramenta = conexao.execute(
            "SELECT id FROM ferramentas WHERE id = ?",
            (pedido.ferramenta_id,)
        ).fetchone()

        if ferramenta is None:
            raise HTTPException(
                status_code=404,
                detail="Ferramenta não encontrada"
            )

        hoje = date.today().isoformat()

        cursor = conexao.execute("""
            INSERT INTO pedidos (
                data, solicitante, ferramenta_id, prazo,
                status, abertura, descricao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            hoje,
            pedido.solicitante,
            pedido.ferramenta_id,
            pedido.prazo,
            "andamento",
            hoje,
            pedido.descricao
        ))

        conexao.commit()

        novo_pedido = conexao.execute(
            "SELECT * FROM pedidos WHERE id = ?",
            (cursor.lastrowid,)
        ).fetchone()

        return dict(novo_pedido)
    finally:
        conexao.close()


# Atualizar pedido
@app.put("/pedidos/{pedido_id}")
def atualizar_pedido(pedido_id: int, dados: PedidoAtualizar):
    conexao = conectar_banco()

    try:
        pedido = conexao.execute(
            "SELECT id FROM pedidos WHERE id = ? AND excluido = 0",
            (pedido_id,)
        ).fetchone()

        if pedido is None:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado"
            )

        if dados.status not in ["andamento", "aguardando", "concluida"]:
            raise HTTPException(
                status_code=400,
                detail="Status inválido"
            )

        atendido = (
            date.today().isoformat()
            if dados.status == "concluida"
            else None
        )

        conexao.execute("""
            UPDATE pedidos
            SET status = ?, feedback = ?, atendido = ?
            WHERE id = ?
        """, (
            dados.status,
            dados.feedback,
            atendido,
            pedido_id
        ))

        conexao.commit()

        atualizado = conexao.execute(
            "SELECT * FROM pedidos WHERE id = ?",
            (pedido_id,)
        ).fetchone()

        return dict(atualizado)
    finally:
        conexao.close()


# Excluir pedido logicamente
@app.delete("/pedidos/{pedido_id}")
def excluir_pedido(pedido_id: int):
    conexao = conectar_banco()

    try:
        pedido = conexao.execute(
            "SELECT id FROM pedidos WHERE id = ? AND excluido = 0",
            (pedido_id,)
        ).fetchone()

        if pedido is None:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado ou já excluído"
            )

        conexao.execute(
            "UPDATE pedidos SET excluido = 1 WHERE id = ?",
            (pedido_id,)
        )

        conexao.commit()

        return {
            "mensagem": "Pedido excluído com sucesso",
            "pedido_id": pedido_id
        }
    finally:
        conexao.close()


# Listar usuarios sem mostrar senhas
@app.get("/usuarios")
def listar_usuarios():
    conexao = conectar_banco()

    try:
        usuarios = conexao.execute("""
            SELECT id, nome, email, perfil
            FROM usuarios
            ORDER BY id
        """).fetchall()

        return [dict(usuario) for usuario in usuarios]
    finally:
        conexao.close()


# Cadastrar usuario com senha protegida
@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: UsuarioCriar):
    if usuario.perfil not in PERFIS_VALIDOS:
        raise HTTPException(
            status_code=400,
            detail="Perfil inválido"
        )

    nome = usuario.nome.strip()

    if not nome:
        raise HTTPException(
            status_code=400,
            detail="O nome não pode estar vazio"
        )

    senha_protegida = password_hash.hash(usuario.senha)

    conexao = conectar_banco()

    try:
        cursor = conexao.execute("""
            INSERT INTO usuarios (nome, email, senha, perfil)
            VALUES (?, ?, ?, ?)
        """, (
            nome,
            str(usuario.email).lower(),
            senha_protegida,
            usuario.perfil
        ))

        conexao.commit()

        novo_usuario = conexao.execute("""
            SELECT id, nome, email, perfil
            FROM usuarios
            WHERE id = ?
        """, (cursor.lastrowid,)).fetchone()

        return dict(novo_usuario)

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Este e-mail já está cadastrado"
        )

    finally:
        conexao.close()


# Atualizar nome, email e perfil de um usuario
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, dados: UsuarioAtualizar):
    if dados.perfil not in PERFIS_VALIDOS:
        raise HTTPException(
            status_code=400,
            detail="Perfil inválido"
        )

    nome = dados.nome.strip()

    if not nome:
        raise HTTPException(
            status_code=400,
            detail="O nome não pode estar vazio"
        )

    conexao = conectar_banco()

    try:
        usuario = conexao.execute(
            "SELECT id FROM usuarios WHERE id = ?",
            (usuario_id,)
        ).fetchone()

        if usuario is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado"
            )

        conexao.execute("""
            UPDATE usuarios
            SET nome = ?, email = ?, perfil = ?
            WHERE id = ?
        """, (
            nome,
            str(dados.email).lower(),
            dados.perfil,
            usuario_id
        ))

        conexao.commit()

        usuario_atualizado = conexao.execute("""
            SELECT id, nome, email, perfil
            FROM usuarios
            WHERE id = ?
        """, (usuario_id,)).fetchone()

        return dict(usuario_atualizado)

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Este e-mail já está cadastrado"
        )

    finally:
        conexao.close()
