# Configuração do Banco MySQL

Este projeto utiliza MySQL com configurações seguras através de variáveis de ambiente.

## Pré-requisitos

### 1. Instalar MySQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mysql-server mysql-client
sudo systemctl start mysql
sudo systemctl enable mysql
```

**macOS (com Homebrew):**
```bash
brew install mysql
brew services start mysql
```

**Windows:**
- Baixe o instalador do [site oficial do MySQL](https://dev.mysql.com/downloads/mysql/)
- Siga o instalador gráfico
- Ou use o MySQL Installer

### 2. Configurar MySQL

1. **Configurar segurança inicial:**
```bash
# Ubuntu/Debian
sudo mysql_secure_installation

# macOS/Windows - executar após instalação
mysql_secure_installation
```

2. **Criar um banco de dados:**
```bash
# Conectar ao MySQL
mysql -u root -p

# Criar banco de dados
CREATE DATABASE exemplo_bd;

# Criar usuário (opcional)
CREATE USER 'meu_usuario'@'localhost' IDENTIFIED BY 'minha_senha';
GRANT ALL PRIVILEGES ON exemplo_bd.* TO 'meu_usuario'@'localhost';
FLUSH PRIVILEGES;

# Sair do MySQL
EXIT;
```

3. **Verificar se o MySQL está rodando:**
```bash
# Linux/Mac
sudo systemctl status mysql
# ou
brew services list | grep mysql

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
DB_USER=root
DB_PASSWORD=sua_senha_do_mysql
DB_PORT=3306
```

### 3. Executar o programa

```bash
python mysql_bd.py
```

## Troubleshooting

### Problemas Comuns

**1. Erro de conexão:**
```
mysql.connector.errors.DatabaseError: 2003 (HY000): Can't connect to MySQL server
```
- Verifique se o MySQL está rodando
- Confirme as credenciais no `config.env`
- Teste a conexão: `mysql -h localhost -u root -p`

**2. Erro de autenticação:**
```
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user
```
- Verifique a senha do usuário
- Teste a conexão manual: `mysql -u root -p`

**3. Banco não existe:**
```
mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'exemplo_bd'
```
- Crie o banco de dados primeiro (veja seção "Configurar MySQL")

**4. Erro de permissão:**
```
mysql.connector.errors.ProgrammingError: 1142 (42000): INSERT command denied to user
```
- Verifique se o usuário tem permissões no banco
- Use `GRANT ALL PRIVILEGES ON exemplo_bd.* TO 'seu_usuario'@'localhost';`

**5. Erro de charset/encoding:**
```
mysql.connector.errors.ProgrammingError: 1366 (HY000): Incorrect string value
```
- Verifique se o banco está configurado com UTF-8
- Use: `ALTER DATABASE exemplo_bd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`

### Comandos Úteis

```bash
# Conectar ao MySQL
mysql -h localhost -u root -p

# Listar bancos de dados
SHOW DATABASES;

# Usar um banco específico
USE exemplo_bd;

# Listar tabelas
SHOW TABLES;

# Descrever estrutura de uma tabela
DESCRIBE pessoa;

# Sair do MySQL
EXIT;
```

## Diferenças entre MySQL e PostgreSQL

### Tipos de Dados
- **MySQL**: `AUTO_INCREMENT` vs PostgreSQL `SERIAL`
- **MySQL**: `INT` vs PostgreSQL `INTEGER`
- **MySQL**: `VARCHAR` vs PostgreSQL `VARCHAR` (similar)
- **MySQL**: `DATETIME` vs PostgreSQL `TIMESTAMP`

### Sintaxe SQL
- **MySQL**: `AUTO_INCREMENT PRIMARY KEY`
- **PostgreSQL**: `SERIAL PRIMARY KEY`
- **MySQL**: `ENGINE=InnoDB` (opcional)
- **PostgreSQL**: Não usa engines

### Conexão
- **MySQL**: Porta padrão 3306
- **PostgreSQL**: Porta padrão 5432
- **MySQL**: `mysql.connector`
- **PostgreSQL**: `psycopg2`

## Segurança

- O arquivo `config.env` está no `.gitignore` e não será commitado
- Use o arquivo `config.env.example` como template para outros desenvolvedores
- Nunca commite credenciais reais no repositório
- Para produção, use variáveis de ambiente do sistema ou serviços de gerenciamento de secrets
- Configure o MySQL com senhas fortes e usuários específicos para cada aplicação

## Performance

### Dicas de Otimização MySQL

1. **Índices:**
```sql
CREATE INDEX idx_nome ON pessoa(nome);
CREATE INDEX idx_categoria ON pessoa(categoria_id);
```

2. **Configuração do MySQL:**
```sql
-- Verificar configurações
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SHOW VARIABLES LIKE 'max_connections';
```

3. **Análise de queries:**
```sql
-- Ativar log de queries lentas
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;
```

## Backup e Restore

### Backup
```bash
# Backup completo do banco
mysqldump -u root -p exemplo_bd > backup_exemplo_bd.sql

# Backup apenas estrutura
mysqldump -u root -p --no-data exemplo_bd > estrutura_exemplo_bd.sql
```

### Restore
```bash
# Restaurar banco
mysql -u root -p exemplo_bd < backup_exemplo_bd.sql
```
