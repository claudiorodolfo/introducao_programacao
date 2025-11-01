"""
DAO (Data Access Object) para operações de banco de dados da tabela categoria
"""
from typing import List, Optional
from bd.database import DatabaseConnection
from model.categoria import Categoria

class CategoriaDAO:
    def __init__(self, db: DatabaseConnection):
        self.db = db
    
    def criarTabela(self):
        cur = self.db.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        );
        """)
        self.db.commit()
    
    def salvar(self, categoria: Categoria):
        cur = self.db.cursor()
        
        if categoria.id is None:
            # INSERT
            cur.execute("INSERT INTO categoria (nome) VALUES (?);", (categoria.nome,))
            categoria.id = cur.lastrowid
        else:
            # UPDATE
            cur.execute("UPDATE categoria SET nome = ? WHERE id = ?;", (categoria.nome, categoria.id))
        
        self.db.commit()
        return categoria.id
    
    def buscarPorId(self, id: int):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM categoria WHERE id = ?;", (id,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def buscarPorNome(self, nome: str):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM categoria WHERE nome = ?;", (nome,))
        row = cur.fetchone()
        
        if row:
            return self.criarDeRow(row)
        return None
    
    def listarTodas(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM categoria ORDER BY nome;")
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def criarDeRow(self, row):
        return Categoria(
            id=row['id'],
            nome=row['nome']
        )
    
    def deletar(self, categoria: Categoria):
        if categoria.id is None:
            return False
        
        cur = self.db.cursor()
        cur.execute("DELETE FROM categoria WHERE id = ?;", (categoria.id,))
        self.db.commit()
        return cur.rowcount > 0

