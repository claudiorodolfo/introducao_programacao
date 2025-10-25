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
# Instalar dependências globalmente
pip3 install -r requirements.txt
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
python3 postgresql_bd.py
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

#### Conectar ao PostgreSQL
```bash
# Conectar como usuário padrão
psql -h localhost -U postgres

# Conectar a um banco específico
psql -h localhost -U postgres -d exemplo_bd

# Conectar com porta específica
psql -h localhost -U postgres -p 5432

# Conectar via socket Unix (Linux/Mac)
psql -U postgres
```

#### Comandos dentro do psql

**Navegação e Informações:**
```sql
-- Listar todos os bancos de dados
\l
\l+

-- Conectar a um banco específico
\c exemplo_bd
\c nome_do_banco

-- Listar tabelas do banco atual
\dt
\dt+

-- Listar todas as tabelas (incluindo system tables)
\dt *

-- Descrever estrutura de uma tabela
\d nome_da_tabela
\d+ nome_da_tabela

-- Listar índices
\di

-- Listar views
\dv

-- Listar funções
\df

-- Listar usuários/roles
\du
\du+

-- Mostrar informações do banco atual
\conninfo

-- Mostrar versão do PostgreSQL
SELECT version();
```

**Consultas e Dados:**
```sql
-- Ver todas as tabelas e suas linhas
SELECT schemaname, tablename, n_tup_ins as "Inserções", n_tup_upd as "Atualizações", n_tup_del as "Deleções" 
FROM pg_stat_user_tables;

-- Ver tamanho das tabelas
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Ver conexões ativas
SELECT pid, usename, application_name, client_addr, state, query 
FROM pg_stat_activity 
WHERE state = 'active';

-- Ver estatísticas do banco
SELECT * FROM pg_stat_database WHERE datname = 'exemplo_bd';
```

**Gerenciamento de Usuários:**
```sql
-- Criar usuário
CREATE USER novo_usuario WITH PASSWORD 'senha_segura';

-- Dar privilégios
GRANT ALL PRIVILEGES ON DATABASE exemplo_bd TO novo_usuario;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO novo_usuario;

-- Alterar senha
ALTER USER nome_usuario WITH PASSWORD 'nova_senha';

-- Remover usuário
DROP USER nome_usuario;
```

**Backup e Restore:**
```bash
# Backup completo do banco
pg_dump -h localhost -U postgres -d exemplo_bd > backup.sql

# Backup apenas estrutura (schema)
pg_dump -h localhost -U postgres -d exemplo_bd --schema-only > schema.sql

# Backup apenas dados
pg_dump -h localhost -U postgres -d exemplo_bd --data-only > dados.sql

# Restaurar backup
psql -h localhost -U postgres -d exemplo_bd < backup.sql

# Backup com compressão
pg_dump -h localhost -U postgres -d exemplo_bd | gzip > backup.sql.gz

# Restaurar backup comprimido
gunzip -c backup.sql.gz | psql -h localhost -U postgres -d exemplo_bd
```

**Configuração e Monitoramento:**
```sql
-- Ver configurações atuais
SHOW ALL;

-- Ver configuração específica
SHOW max_connections;
SHOW shared_buffers;

-- Ver logs de erro recentes (se habilitado)
SELECT * FROM pg_stat_database;

-- Ver queries lentas (se pg_stat_statements estiver habilitado)
SELECT query, calls, total_time, mean_time 
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;
```

**Comandos de Sistema:**
```bash
# Iniciar PostgreSQL
sudo systemctl start postgresql    # Linux
brew services start postgresql     # macOS

# Parar PostgreSQL
sudo systemctl stop postgresql     # Linux
brew services stop postgresql      # macOS

# Reiniciar PostgreSQL
sudo systemctl restart postgresql  # Linux
brew services restart postgresql   # macOS

# Ver status do serviço
sudo systemctl status postgresql   # Linux
brew services list | grep postgresql  # macOS

# Ver logs do PostgreSQL
sudo tail -f /var/log/postgresql/postgresql-*.log  # Linux
tail -f /usr/local/var/log/postgresql.log          # macOS (Homebrew)
```

**Sair do psql:**
```sql
-- Qualquer um destes comandos funciona
\q
exit
quit
```

## Segurança

- O arquivo `config.env` está no `.gitignore` e não será commitado
- Use o arquivo `config.env.example` como template para outros desenvolvedores
- Nunca commite credenciais reais no repositório
- Para produção, use variáveis de ambiente do sistema ou serviços de gerenciamento de secrets