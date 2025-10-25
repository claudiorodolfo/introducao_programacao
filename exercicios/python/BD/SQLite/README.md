# Configuração do Banco SQLite

Este projeto utiliza SQLite com configurações seguras através de variáveis de ambiente.

## Pré-requisitos

### 1. SQLite já vem incluído no Python

O SQLite é um banco de dados embarcado que já vem incluído com Python, não necessitando instalação adicional.

**Verificar se SQLite está disponível:**
```bash
python3 -c "import sqlite3; print('SQLite disponível!')"
```

### 2. Ferramentas opcionais para gerenciar SQLite

**SQLite Browser (DB Browser for SQLite):**
- **Ubuntu/Debian:** `sudo apt install sqlitebrowser`
- **macOS:** `brew install --cask db-browser-for-sqlite`
- **Windows:** Baixe do [site oficial](https://sqlitebrowser.org/)

**SQLite CLI:**
```bash
# Verificar versão
sqlite3 --version

# Conectar a um banco
sqlite3 exemplo_bd.db
```

## Configuração do Projeto

### 1. Executar o programa

Como o SQLite é um banco embarcado e não precisa de configurações especiais, você pode executar diretamente:

```bash
python sqlite_bd.py
```

O programa criará automaticamente o arquivo `exemplo_bd.db` no mesmo diretório.

## Troubleshooting

### Problemas Comuns

**1. Erro de permissão:**
```
sqlite3.OperationalError: unable to open database file
```
- Verifique se o diretório tem permissão de escrita
- Use um caminho absoluto no `config.env`

**2. Banco corrompido:**
```
sqlite3.DatabaseError: database disk image is malformed
```
- Faça backup do banco: `cp exemplo_bd.db backup_exemplo_bd.db`
- Recrie o banco executando o script novamente

**3. Erro de encoding:**
```
sqlite3.OperationalError: Could not decode to UTF-8
```
- SQLite usa UTF-8 por padrão
- Verifique se os dados inseridos estão em UTF-8

### Comandos Úteis

```bash
# Conectar ao banco SQLite
sqlite3 exemplo_bd.db

# Listar tabelas
.tables

# Descrever estrutura de uma tabela
.schema pessoa

# Ver dados de uma tabela
SELECT * FROM pessoa;

# Sair do SQLite
.quit
```

## Diferenças entre SQLite e outros SGBDs

### Tipos de Dados
- **SQLite**: `INTEGER` vs MySQL `INT` vs PostgreSQL `INTEGER`
- **SQLite**: `TEXT` vs MySQL `VARCHAR` vs PostgreSQL `VARCHAR`
- **SQLite**: `REAL` vs MySQL `FLOAT` vs PostgreSQL `REAL`
- **SQLite**: `INTEGER` para BOOLEAN vs MySQL `BOOLEAN` vs PostgreSQL `BOOLEAN`

### Sintaxe SQL
- **SQLite**: `INTEGER PRIMARY KEY AUTOINCREMENT`
- **MySQL**: `INT AUTO_INCREMENT PRIMARY KEY`
- **PostgreSQL**: `SERIAL PRIMARY KEY`
- **SQLite**: Não tem tipos DATE/TIME nativos (usa TEXT)
- **SQLite**: Não tem tipos DECIMAL nativos (usa REAL)

### Conexão
- **SQLite**: Arquivo local, não precisa de servidor
- **MySQL**: Servidor na porta 3306
- **PostgreSQL**: Servidor na porta 5432
- **SQLite**: `sqlite3` (built-in)
- **MySQL**: `mysql.connector`
- **PostgreSQL**: `psycopg2`

## Vantagens do SQLite

### 1. **Simplicidade**
- Não precisa de servidor
- Arquivo único contém todo o banco
- Fácil de fazer backup (copiar arquivo)

### 2. **Portabilidade**
- Funciona em qualquer sistema operacional
- Não precisa de instalação adicional
- Ideal para desenvolvimento e testes

### 3. **Performance**
- Muito rápido para operações simples
- Ideal para aplicações pequenas e médias
- Baixo consumo de recursos

### 4. **Confiabilidade**
- Transações ACID
- Resistente a falhas
- Usado em produção por grandes empresas

## Limitações do SQLite

### 1. **Concorrência**
- Suporte limitado a múltiplos escritores simultâneos
- Ideal para aplicações com poucos usuários simultâneos

### 2. **Recursos Avançados**
- Não tem stored procedures
- Não tem triggers complexos
- Não tem usuários/permissões

### 3. **Escalabilidade**
- Não é ideal para aplicações com milhões de usuários
- Limite prático de ~100GB por banco

## Segurança

- SQLite não tem autenticação nativa - proteja o arquivo do banco
- Para produção, use caminhos seguros e backups regulares
- Nunca commite arquivos de banco de dados no repositório

## Performance

### Dicas de Otimização SQLite

1. **Índices:**
```sql
CREATE INDEX idx_nome ON pessoa(nome);
CREATE INDEX idx_categoria ON pessoa(categoria_id);
```

2. **Configurações do SQLite:**
```sql
-- Ativar WAL mode para melhor concorrência
PRAGMA journal_mode=WAL;

-- Configurar cache
PRAGMA cache_size=10000;

-- Otimizar para performance
PRAGMA optimize;
```

3. **Análise de queries:**
```sql
-- Ativar explain query plan
EXPLAIN QUERY PLAN SELECT * FROM pessoa WHERE nome = 'Ana';
```

## Backup e Restore

### Backup
```bash
# Backup simples (copiar arquivo)
cp exemplo_bd.db backup_exemplo_bd.db

# Backup com SQLite CLI
sqlite3 exemplo_bd.db ".backup backup_exemplo_bd.db"

# Dump SQL
sqlite3 exemplo_bd.db ".dump" > backup_exemplo_bd.sql
```

### Restore
```bash
# Restaurar de arquivo
cp backup_exemplo_bd.db exemplo_bd.db

# Restaurar de dump SQL
sqlite3 novo_banco.db < backup_exemplo_bd.sql
```

## Casos de Uso Ideais

### ✅ **SQLite é ideal para:**
- Aplicações desktop
- Aplicações móveis
- Prototipagem rápida
- Desenvolvimento e testes
- Aplicações com poucos usuários
- Sistemas embarcados
- Cache local

### ❌ **SQLite NÃO é ideal para:**
- Aplicações web com muitos usuários
- Sistemas que precisam de múltiplos escritores
- Aplicações que precisam de recursos avançados
- Sistemas distribuídos
