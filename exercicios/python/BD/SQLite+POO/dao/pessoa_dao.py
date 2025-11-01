"""
DAO (Data Access Object) para operações de banco de dados da tabela pessoa
"""

from bd.database import DatabaseConnection
from dao.categoria_dao import CategoriaDAO
from model.pessoa import Pessoa
from model.categoria import Categoria

class PessoaDAO:
    def __init__(self, db: DatabaseConnection):
        self.db = db
    
    def criarTabela(self):
        cur = self.db.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS pessoa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER CHECK (idade >= 0 AND idade <= 120),
            altura REAL,
            peso REAL,
            data_nascimento TEXT,
            ativo INTEGER DEFAULT 1,
            observacoes TEXT,
            telefone TEXT,
            categoria_id INTEGER NOT NULL,
            momento_cadastro TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        );
        """)
    
    def salvar(self, pessoa: Pessoa):
        cur = self.db.cursor()
        
        # Converter boolean para integer (SQLite)
        ativo_int = 1 if pessoa.ativo else 0
        
        categoria_id = pessoa.categoria.id
        
        if pessoa.id is None:
            # INSERT
            cur.execute("""
                INSERT INTO pessoa (nome, email, idade, altura, peso, data_nascimento,
                                 ativo, observacoes, telefone, categoria_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (pessoa.nome, pessoa.email, pessoa.idade, pessoa.altura, pessoa.peso,
                  pessoa.data_nascimento, ativo_int, pessoa.observacoes, pessoa.telefone,
                  categoria_id))

            pessoa.id = cur.lastrowid
        else:
            # UPDATE
            cur.execute("""
                UPDATE pessoa SET nome = ?, email = ?, idade = ?, altura = ?, peso = ?,
                               data_nascimento = ?, ativo = ?, observacoes = ?,
                               telefone = ?, categoria_id = ?
                WHERE id = ?;
            """, (pessoa.nome, pessoa.email, pessoa.idade, pessoa.altura, pessoa.peso,
                  pessoa.data_nascimento, ativo_int, pessoa.observacoes, pessoa.telefone,
                  categoria_id, pessoa.id))
        
        return pessoa.id
    
    def buscarPorId(self, id: int):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM pessoa WHERE id = ?;", (id,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def buscarPorNome(self, nome: str):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM pessoa WHERE nome LIKE ?;", (f'%{nome}%',))
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def listarTodas(self, com_categoria: bool = False):
        cur = self.db.cursor()
        
        if com_categoria:
            cur.execute("""
                SELECT p.*, c.nome as categoria_nome
                FROM pessoa p
                JOIN categoria c ON p.categoria_id = c.id
                ORDER BY p.nome;
            """)
        else:
            cur.execute("SELECT * FROM pessoa ORDER BY nome;")
        
        rows = cur.fetchall()
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def buscarPorCategoria(self, categoria_id: int):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM pessoa WHERE categoria_id = ? ORDER BY nome;", (categoria_id,))
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def criarDeRow(self, row):
        # Buscar a categoria usando o CategoriaDAO
        categoria_dao = CategoriaDAO(self.db)
        categoria = categoria_dao.buscarPorId(row['categoria_id'])
        
        return Pessoa(
            id=row['id'],
            nome=row['nome'],
            email=row['email'],
            idade=row['idade'],
            altura=row['altura'],
            peso=row['peso'],
            data_nascimento=row['data_nascimento'],
            ativo=bool(row['ativo']),
            observacoes=row['observacoes'],
            telefone=row['telefone'],
            categoria=categoria,
            momento_cadastro=row['momento_cadastro']
        )
    
    def deletar(self, pessoa: Pessoa):        
        cur = self.db.cursor()
        cur.execute("DELETE FROM pessoa WHERE id = ?;", (pessoa.id,))

        return cur.rowcount > 0
    
    def obterCategoria(self, pessoa: Pessoa):
        return pessoa.categoria

