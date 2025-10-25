# Configuração do Banco PostgreSQL

Este projeto utiliza PostgreSQL com configurações seguras através de variáveis de ambiente.

## Pré-requisitos

### 1. Instalar PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**macOS (com Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
- Baixe o instalador do [site oficial do PostgreSQL](https://www.postgresql.org/download/windows/)
- Siga o instalador gráfico

### 2. Configurar PostgreSQL

1. **Criar um banco de dados:**
```bash
# Conectar ao PostgreSQL
sudo -u postgres psql

# Criar banco de dados
CREATE DATABASE exemplo_bd;

# Criar usuário (opcional)
CREATE USER meu_usuario WITH PASSWORD 'minha_senha';
GRANT ALL PRIVILEGES ON DATABASE exemplo_bd TO meu_usuario;

# Sair do psql
\q
```

2. **Verificar se o PostgreSQL está rodando:**
```bash
# Linux/Mac
sudo systemctl status postgresql
# ou
brew services list | grep postgresql

# Windows - verificar no Services (services.msc)
```

## Configuração do Projeto

### 1. Instalar dependências Python

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar credenciais do banco

1. Copie o arquivo de exemplo:
```bash
cp config.env.example config.env
```

2. Edite o arquivo `config.env` com suas credenciais:
```env
DB_HOST=localhost
DB_NAME=exemplo_bd
DB_USER=postgres
DB_PASSWORD=sua_senha_do_postgres
DB_PORT=5432
```

### 3. Executar o programa

```bash
python postgresql_bd.py
```

## Troubleshooting

### Problemas Comuns

**1. Erro de conexão:**
```
psycopg2.OperationalError: could not connect to server
```
- Verifique se o PostgreSQL está rodando
- Confirme as credenciais no `config.env`
- Teste a conexão: `psql -h localhost -U postgres -d exemplo_bd`

**2. Erro de autenticação:**
```
psycopg2.OperationalError: FATAL: password authentication failed
```
- Verifique a senha do usuário
- No Linux, pode ser necessário configurar `pg_hba.conf`

**3. Banco não existe:**
```
psycopg2.OperationalError: database "exemplo_bd" does not exist
```
- Crie o banco de dados primeiro (veja seção "Configurar PostgreSQL")

**4. Erro de permissão:**
```
psycopg2.OperationalError: permission denied for database
```
- Verifique se o usuário tem permissões no banco
- Use `GRANT ALL PRIVILEGES ON DATABASE exemplo_bd TO seu_usuario;`

### Comandos Úteis

```bash
# Conectar ao PostgreSQL
psql -h localhost -U postgres

# Listar bancos de dados
\l

# Conectar a um banco específico
\c exemplo_bd

# Listar tabelas
\dt

# Sair do psql
\q
```

## Segurança

- O arquivo `config.env` está no `.gitignore` e não será commitado
- Use o arquivo `config.env.example` como template para outros desenvolvedores
- Nunca commite credenciais reais no repositório
- Para produção, use variáveis de ambiente do sistema ou serviços de gerenciamento de secrets