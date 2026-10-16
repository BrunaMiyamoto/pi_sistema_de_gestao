
import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("database.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabelas():
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()

        # Tabela de usuários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                perfil TEXT NOT NULL DEFAULT 'solicitante'
            )
        """)

        # Atualizar bancos antigos sem perder usuários
        colunas_usuarios = [
            coluna["name"]
            for coluna in cursor.execute(
                "PRAGMA table_info(usuarios)"
            ).fetchall()
        ]

        if "perfil" not in colunas_usuarios:
            cursor.execute("""
                ALTER TABLE usuarios
                ADD COLUMN perfil TEXT NOT NULL
                DEFAULT 'solicitante'
            """)

        # Tabela de ferramentas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ferramentas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        # Tabela de pedidos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                solicitante TEXT NOT NULL,
                ferramenta_id INTEGER NOT NULL,
                prazo TEXT NOT NULL,
                status TEXT NOT NULL,
                abertura TEXT NOT NULL,
                atendido TEXT,
                feedback TEXT,
                descricao TEXT,
                excluido INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (ferramenta_id)
                    REFERENCES ferramentas (id)
            )
        """)

        # Atualizar bancos antigos sem perder pedidos
        colunas_pedidos = [
            coluna["name"]
            for coluna in cursor.execute(
                "PRAGMA table_info(pedidos)"
            ).fetchall()
        ]

        if "excluido" not in colunas_pedidos:
            cursor.execute("""
                ALTER TABLE pedidos
                ADD COLUMN excluido INTEGER NOT NULL DEFAULT 0
            """)

        # Ferramentas disponíveis
        ferramentas = [
            "Molde de injeção convencional",
            "Molde de sopro",
            "Molde de borracha",
            "Molde de rotomoldagem",
            "Molde de termoformagem",
            "Ferramentas de Fundição",
            "Dispositivos",
            "Outros"
        ]

        cursor.executemany("""
            INSERT OR IGNORE INTO ferramentas (nome)
            VALUES (?)
        """, [(ferramenta,) for ferramenta in ferramentas])

        conexao.commit()

    finally:
        conexao.close()
