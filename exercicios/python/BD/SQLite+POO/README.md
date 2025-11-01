# Projeto SQLite com Programação Orientada a Objetos (POO)

Sistema completo de gerenciamento de pessoas e categorias utilizando SQLite como banco de dados e implementando padrões de projeto como DAO (Data Access Object) e Services.

## 📋 Índice

- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Usar](#como-usar)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Modelos de Dados](#modelos-de-dados)
- [Operações CRUD](#operações-crud)
- [Exemplos de Uso](#exemplos-de-uso)
- [Testes](#testes)
- [Comandos SQLite Úteis](#comandos-sqlite-úteis)
- [Troubleshooting](#troubleshooting)

## 📁 Estrutura do Projeto

```
SQLite+POO/
├── bd/
│   └── database.py           # Classe DatabaseConnection para gerenciar conexões
├── model/
│   ├── pessoa.py             # Modelo da entidade Pessoa
│   └── categoria.py          # Modelo da entidade Categoria
├── dao/
│   ├── pessoa_dao.py         # DAO para operações de banco de Pessoa
│   └── categoria_dao.py      # DAO para operações de banco de Categoria
├── app/
│   ├── PessoaService.py      # Serviço interativo para gerenciar pessoas
│   └── CategoriaService.py   # Serviço interativo para gerenciar categorias
├── exemplo_uso_orm.py        # Exemplo completo de uso das classes
├── teste_projeto.py          # Suite de testes automatizados
├── exemplo_bd.db             # Arquivo do banco de dados SQLite (gerado automaticamente)
└── README.md                 # Este arquivo
```

## 🔧 Pré-requisitos

### 1. Python 3.7+

O SQLite já vem incluído no Python, não necessitando instalação adicional.

**Verificar se Python e SQLite estão disponíveis:**
```bash
python3 --version
python3 -c "import sqlite3; print('SQLite disponível!')"
```

### 2. Ferramentas Opcionais para Gerenciar SQLite

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

## 🚀 Instalação e Configuração

1. **Clone ou baixe o projeto**

2. **Navegue até o diretório:**
```bash
cd SQLite+POO
```

3. **Pronto!** O projeto está configurado. O banco de dados será criado automaticamente na primeira execução.

## 💻 Como Usar

### Executar Serviços Interativos

#### Gerenciar Pessoas
```bash
python3 app/PessoaService.py
```

Menu disponível:
- Criar pessoa
- Listar todas as pessoas
- Buscar pessoa por ID
- Buscar pessoa por nome
- Buscar pessoas por categoria
- Atualizar pessoa
- Deletar pessoa

#### Gerenciar Categorias
```bash
python3 app/CategoriaService.py
```

Menu disponível:
- Criar categoria
- Listar todas as categorias
- Buscar categoria por ID
- Buscar categoria por nome
- Atualizar categoria
- Deletar categoria

### Executar Exemplo Completo

Demonstra operações CRUD completas usando as classes diretamente:

```bash
python3 exemplo_uso_orm.py
```

### Executar Testes

Executa suite completa de testes automatizados:

```bash
python3 teste_projeto.py
```

Os testes verificam:
- ✅ Operações CRUD de Categoria
- ✅ Operações CRUD de Pessoa
- ✅ Integridade referencial e constraints

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura em camadas seguindo o padrão **DAO (Data Access Object)**:

### Camada de Banco de Dados (`bd/`)
- **`DatabaseConnection`**: Gerencia conexões com SQLite
  - Conexão singleton
  - Configuração de foreign keys
  - Row factory para retornar dicionários
  - Criação automática de tabelas
  - Limpeza de dados para testes

### Camada de Modelo (`model/`)
- **`Categoria`**: Entidade categoria (id, nome)
- **`Pessoa`**: Entidade pessoa com todos os atributos e relacionamento com Categoria

### Camada de Acesso a Dados (`dao/`)
- **`CategoriaDAO`**: Operações CRUD para Categoria
  - `salvar()` - Insere ou atualiza
  - `buscarPorId()` - Busca por ID
  - `buscarPorNome()` - Busca por nome exato
  - `listarTodas()` - Lista todas as categorias
  - `deletar()` - Remove categoria
  - `criarTabela()` - Cria estrutura da tabela

- **`PessoaDAO`**: Operações CRUD para Pessoa
  - `salvar()` - Insere ou atualiza
  - `buscarPorId()` - Busca por ID
  - `buscarPorNome()` - Busca por nome (LIKE)
  - `buscarPorCategoria()` - Busca pessoas de uma categoria
  - `listarTodas()` - Lista todas as pessoas (com opção de JOIN com categoria)
  - `deletar()` - Remove pessoa
  - `obterCategoria()` - Obtém categoria relacionada
  - `criarTabela()` - Cria estrutura da tabela

### Camada de Aplicação (`app/`)
- **`PessoaService`**: Interface interativa via CLI para gerenciar pessoas
- **`CategoriaService`**: Interface interativa via CLI para gerenciar categorias

## 📊 Modelos de Dados

### Tabela: `categoria`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (auto-increment) |
| nome | TEXT | Nome da categoria (UNIQUE, NOT NULL) |

### Tabela: `pessoa`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (auto-increment) |
| nome | TEXT | Nome da pessoa (NOT NULL) |
| email | TEXT | Email único (UNIQUE, NOT NULL) |
| idade | INTEGER | Idade (0-120) |
| altura | REAL | Altura em metros |
| peso | REAL | Peso em kg |
| data_nascimento | TEXT | Data no formato AAAA-MM-DD |
| ativo | INTEGER | Status ativo/inativo (1/0) |
| observacoes | TEXT | Observações sobre a pessoa |
| telefone | TEXT | Número de telefone |
| categoria_id | INTEGER | Foreign Key para categoria (NOT NULL) |
| momento_cadastro | TEXT | Timestamp de criação (DEFAULT CURRENT_TIMESTAMP) |

### Relacionamentos

- **Pessoa → Categoria**: Relacionamento Many-to-One (N pessoas pertencem a 1 categoria)
- **Foreign Key**: `pessoa.categoria_id` referencia `categoria.id`

## 🔄 Operações CRUD

### Criar (Create)

```python
from bd.database import DatabaseConnection
from model.categoria import Categoria
from model.pessoa import Pessoa
from dao.categoria_dao import CategoriaDAO
from dao.pessoa_dao import PessoaDAO

db = DatabaseConnection('exemplo_bd.db')
db.conectar()
db.criarTabelas()

# Criar categoria
categoriaDao = CategoriaDAO(db)
categoria = Categoria(id=None, nome="Desenvolvedor")
categoriaDao.salvar(categoria)

# Criar pessoa
pessoaDao = PessoaDAO(db)
pessoa = Pessoa(
    id=None,
    nome="João Silva",
    email="joao@example.com",
    categoria=categoria,
    idade=28,
    altura=1.75,
    peso=75.0,
    ativo=True
)
pessoaDao.salvar(pessoa)
```

### Ler (Read)

```python
# Buscar por ID
categoria = categoriaDao.buscarPorId(1)
pessoa = pessoaDao.buscarPorId(1)

# Buscar por nome
categoria = categoriaDao.buscarPorNome("Desenvolvedor")
pessoas = pessoaDao.buscarPorNome("João")  # Busca parcial

# Listar todas
categorias = categoriaDao.listarTodas()
pessoas = pessoaDao.listarTodas()

# Buscar por categoria
pessoas = pessoaDao.buscarPorCategoria(categoria.id)
```

### Atualizar (Update)

```python
# Atualizar categoria
categoria.nome = "Desenvolvedor Senior"
categoriaDao.salvar(categoria)

# Atualizar pessoa
pessoa.idade = 29
pessoa.ativo = False
pessoaDao.salvar(pessoa)
```

### Deletar (Delete)

```python
# Deletar pessoa
pessoaDao.deletar(pessoa)

# Deletar categoria
categoriaDao.deletar(categoria)
```

## 📝 Exemplos de Uso

### Exemplo 1: Uso Completo

Execute o arquivo `exemplo_uso_orm.py` para ver um exemplo completo de todas as operações:

```bash
python3 exemplo_uso_orm.py
```

### Exemplo 2: Uso Programático

```python
from bd.database import DatabaseConnection
from model.categoria import Categoria
from model.pessoa import Pessoa
from dao.categoria_dao import CategoriaDAO
from dao.pessoa_dao import PessoaDAO

# Inicializar
db = DatabaseConnection('exemplo_bd.db')
db.conectar()
db.criarTabelas()

# DAOs
categoriaDao = CategoriaDAO(db)
pessoaDao = PessoaDAO(db)

# Criar categoria
cat = Categoria(id=None, nome="Designer")
categoriaDao.salvar(cat)

# Criar pessoa
pessoa = Pessoa(
    id=None,
    nome="Maria Santos",
    email="maria@example.com",
    categoria=cat,
    idade=25,
    altura=1.65
)
pessoaDao.salvar(pessoa)

# Buscar e exibir
pessoaEncontrada = pessoaDao.buscarPorId(pessoa.id)
print(pessoaEncontrada)
print(f"Categoria: {pessoaEncontrada.categoria.nome}")

# Fechar conexão
db.fechar()
```

## 🧪 Testes

O projeto inclui uma suite completa de testes automatizados:

```bash
python3 teste_projeto.py
```

**Testes incluídos:**
1. **Teste de Categoria CRUD**
   - Criar, ler, atualizar e deletar categorias
   - Validação de constraints (UNIQUE)

2. **Teste de Pessoa CRUD**
   - Criar, ler, atualizar e deletar pessoas
   - Busca por nome e categoria
   - Validação de relacionamentos

3. **Teste de Integridade Referencial**
   - Validação de foreign keys
   - Constraints UNIQUE
   - Validações de dados

## 🗄️ Comandos SQLite Úteis

### Conexão e Navegação
```bash
# Conectar ao banco
sqlite3 exemplo_bd.db

# Sair
.quit
.exit
```

### Informações do Banco
```sql
-- Listar todas as tabelas
.tables

-- Ver estrutura de uma tabela
.schema pessoa
.schema categoria

-- Ver todas as estruturas
.schema
```

### Consultas
```sql
-- Ver todos os dados
SELECT * FROM pessoa;
SELECT * FROM categoria;

-- Ver pessoas com suas categorias (JOIN)
SELECT p.id, p.nome, p.email, c.nome as categoria
FROM pessoa p
JOIN categoria c ON p.categoria_id = c.id;

-- Contar registros
SELECT COUNT(*) FROM pessoa;
SELECT COUNT(*) FROM categoria;

-- Buscar pessoas de uma categoria
SELECT p.* FROM pessoa p
WHERE p.categoria_id = 1;
```

### Backup e Restore
```bash
# Backup completo
sqlite3 exemplo_bd.db ".backup backup_exemplo_bd.db"

# Dump SQL
sqlite3 exemplo_bd.db ".dump" > backup_exemplo_bd.sql

# Restaurar
sqlite3 novo_banco.db < backup_exemplo_bd.sql
```

### Manutenção
```sql
-- Otimizar banco
VACUUM;

-- Verificar integridade
PRAGMA integrity_check;

-- Ver estatísticas
ANALYZE;
```

## 🔍 Troubleshooting

### Problemas Comuns

**1. Erro de permissão:**
```
sqlite3.OperationalError: unable to open database file
```
- Verifique se o diretório tem permissão de escrita
- Verifique se o caminho do banco está correto

**2. Banco corrompido:**
```
sqlite3.DatabaseError: database disk image is malformed
```
- Faça backup: `cp exemplo_bd.db backup_exemplo_bd.db`
- Recrie o banco executando os scripts novamente
- Execute: `PRAGMA integrity_check;`

**3. Erro de foreign key:**
```
sqlite3.IntegrityError: FOREIGN KEY constraint failed
```
- Verifique se a categoria existe antes de criar uma pessoa
- Certifique-se de que `PRAGMA foreign_keys = ON` está ativo

**4. Email duplicado:**
```
sqlite3.IntegrityError: UNIQUE constraint failed: pessoa.email
```
- O email deve ser único. Verifique se já existe uma pessoa com esse email

**5. Erro de importação:**
```
ModuleNotFoundError: No module named 'bd'
```
- Certifique-se de estar no diretório correto
- Verifique se todos os arquivos `__pycache__` foram gerados corretamente
- Execute o script a partir do diretório raiz do projeto

## 📚 Padrões de Projeto Utilizados

### DAO (Data Access Object)
Separa a lógica de acesso a dados da lógica de negócio. Cada entidade tem seu próprio DAO.

### Service Layer
Camada de serviços que oferece interfaces amigáveis para interação com o usuário e orquestra chamadas aos DAOs.

### Repository Pattern
Os DAOs funcionam como repositórios, abstraindo a complexidade do banco de dados.

## ⚙️ Configurações do SQLite

O projeto utiliza as seguintes configurações:

- **Foreign Keys**: Ativado automaticamente (`PRAGMA foreign_keys = ON`)
- **Row Factory**: `sqlite3.Row` para retornar objetos similares a dicionários
- **Auto Commit**: `isolation_level=None` para autocommit automático
- **Timestamps**: Uso de `CURRENT_TIMESTAMP` para `momento_cadastro`

## 🔐 Segurança

- SQLite não tem autenticação nativa - proteja o arquivo do banco
- Use caminhos seguros para o arquivo do banco
- Faça backups regulares
- Nunca commite arquivos de banco de dados no repositório (adicione ao `.gitignore`)

## 🚀 Performance

### Dicas de Otimização

1. **Índices:**
```sql
CREATE INDEX idx_nome ON pessoa(nome);
CREATE INDEX idx_email ON pessoa(email);
CREATE INDEX idx_categoria ON pessoa(categoria_id);
```

2. **Configurações:**
```sql
-- Ativar WAL mode (melhor concorrência)
PRAGMA journal_mode=WAL;

-- Aumentar cache
PRAGMA cache_size=10000;
```

3. **Análise de Queries:**
```sql
-- Ver plano de execução
EXPLAIN QUERY PLAN SELECT * FROM pessoa WHERE nome = 'João';
```

## 🎯 Casos de Uso Ideais

### ✅ SQLite é ideal para:
- ✅ Aplicações desktop
- ✅ Prototipagem rápida
- ✅ Desenvolvimento e testes
- ✅ Aplicações com poucos usuários simultâneos
- ✅ Sistemas embarcados
- ✅ Projetos educacionais (como este)

### ❌ SQLite NÃO é ideal para:
- ❌ Aplicações web com muitos usuários
- ❌ Sistemas que precisam de múltiplos escritores simultâneos
- ❌ Aplicações que precisam de recursos avançados (stored procedures, triggers complexos)
- ❌ Sistemas distribuídos

## 📖 Diferenças entre SQLite e outros SGBDs

### Tipos de Dados
- **SQLite**: `INTEGER`, `TEXT`, `REAL`
- **MySQL**: `INT`, `VARCHAR`, `FLOAT`
- **PostgreSQL**: `INTEGER`, `VARCHAR`, `FLOAT`

### Sintaxe SQL
- **SQLite**: `INTEGER PRIMARY KEY AUTOINCREMENT`
- **MySQL**: `INT AUTO_INCREMENT PRIMARY KEY`
- **PostgreSQL**: `SERIAL PRIMARY KEY`

### BOOLEAN
- **SQLite**: Usa `INTEGER` (0/1)
- **MySQL/PostgreSQL**: Têm tipo `BOOLEAN` nativo

## 🤝 Contribuindo

Este é um projeto educacional. Para melhorias:
1. Mantenha a estrutura de camadas
2. Siga os padrões DAO e Service
3. Adicione testes para novas funcionalidades
4. Documente alterações significativas

## 📄 Licença

Projeto educacional - livre para uso e modificação.

---

**Desenvolvido para fins educacionais** 🎓
