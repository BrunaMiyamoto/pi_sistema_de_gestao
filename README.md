
# JactoFlow — Backend

Sistema de gestão de solicitações desenvolvido como Projeto Integrador da UNIVESP.

O projeto tem como objetivo auxiliar o setor de Ferramentaria do Grupo Jacto no registro, acompanhamento e gerenciamento de solicitações.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- pwdlib com Argon2

## Funcionalidades implementadas

### Ferramentas
- Listagem dos tipos de ferramentas disponíveis.

### Pedidos
- Cadastro de solicitações.
- Listagem de pedidos ativos.
- Atualização de status e feedback.
- Exclusão lógica de pedidos, preservando o histórico.

### Usuários
- Cadastro de usuários.
- Listagem de usuários sem exposição das senhas.
- Atualização de nome, e-mail e perfil.
- Armazenamento de senhas com hash Argon2.

## Perfis de usuários

O sistema prevê três perfis:

- `administrador`
- `funcionario`
- `solicitante`

A autenticação e as permissões de acesso ainda não foram implementadas.

## Estrutura do projeto

```text
pi_sistema_de_gestao_backend/
├── main.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

O banco `database.db` é criado localmente na inicialização da API e não deve ser enviado ao GitHub.

## Como executar o backend

### 1. Clonar o repositório

```bash
git clone https://github.com/BrunaMiyamoto/pi_sistema_de_gestao_backend.git
```

Entre na pasta do projeto:

```bash
cd pi_sistema_de_gestao_backend
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução de scripts, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois, tente ativar o ambiente novamente.

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Iniciar o servidor

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

http://127.0.0.1:8000

Documentação interativa:

http://127.0.0.1:8000/docs

## Endpoints disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Verificar funcionamento da API |
| GET | `/ferramentas` | Listar ferramentas |
| GET | `/pedidos` | Listar pedidos ativos |
| POST | `/pedidos` | Cadastrar pedido |
| PUT | `/pedidos/{pedido_id}` | Atualizar status e feedback |
| DELETE | `/pedidos/{pedido_id}` | Excluir pedido logicamente |
| GET | `/usuarios` | Listar usuários |
| POST | `/usuarios` | Cadastrar usuário |
| PUT | `/usuarios/{usuario_id}` | Atualizar usuário |

## Exemplos de requisições

### Cadastrar pedido

POST `/pedidos`

```json
{
  "solicitante": "Engenharia - Jacto Agrícola",
  "ferramenta_id": 1,
  "prazo": "2026-11-20",
  "descricao": "Solicitação de fabricação de molde."
}
```

### Atualizar pedido

PUT `/pedidos/1`

```json
{
  "status": "concluida",
  "feedback": "Serviço finalizado e entregue."
}
```

Status aceitos:

- `andamento`
- `aguardando`
- `concluida`

### Cadastrar usuário

POST `/usuarios`

```json
{
  "nome": "Usuario Teste",
  "email": "usuario.teste@example.com",
  "senha": "SenhaDeTeste123!",
  "perfil": "solicitante"
}
```

Use somente dados fictícios nos testes locais.

## Banco de dados

O projeto utiliza SQLite e possui três tabelas principais:

- `usuarios`: informações e perfis dos usuários.
- `ferramentas`: tipos de ferramentas disponíveis.
- `pedidos`: solicitações cadastradas e seus estados.

A coluna `excluido` permite preservar pedidos removidos da listagem ativa:

- `0`: pedido ativo.
- `1`: pedido excluído logicamente.

## Limitações atuais

Esta versão representa um backend inicial para o MVP acadêmico.

Ainda estão pendentes:

- Login e autenticação.
- Controle efetivo de permissões por perfil.
- Integração com o frontend Vue.
- Recebimento e armazenamento de arquivos técnicos.
- Testes automatizados.

**Atenção:** os endpoints de gerenciamento ainda não estão protegidos por autenticação. Não disponibilizar a API publicamente para uso real antes de implementar controles de acesso e revisar a segurança.

## Projeto Integrador — UNIVESP

Backend desenvolvido para o sistema de gestão de solicitações da Ferramentaria do Grupo Jacto.
