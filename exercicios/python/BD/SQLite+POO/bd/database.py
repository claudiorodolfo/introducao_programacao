"""
Classe para gerenciar conexão com o banco de dados SQLite
"""
import sqlite3

class DatabaseConnection:
    def __init__(self, db_path: str = 'exemplo_bd.db'):
        self.db_path = db_path
        self.conn = None
    
    def conectar(self):
        if self.conn is None:
            # isolation_level=None ativa autocommit (cada operação é commitada automaticamente)
            self.conn = sqlite3.connect(self.db_path, isolation_level=None)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn
    
    def fechar(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            self.conn = None
    

    
    def cursor(self):
        """Retorna um cursor para executar queries"""
        if self.conn is None:
            self.conectar()
        return self.conn.cursor()
    
    def criarTabelas(self):
        # Importar aqui para evitar importação circular
        from dao.categoria_dao import CategoriaDAO
        from dao.pessoa_dao import PessoaDAO
        
        # Tabela categoria
        categoria_dao = CategoriaDAO(self)
        categoria_dao.criarTabela()
        
        # Tabela pessoa
        pessoa_dao = PessoaDAO(self)
        pessoa_dao.criarTabela()
    
    def limparDados(self):
        cur = self.cursor()
        cur.execute("DELETE FROM pessoa;")
        cur.execute("DELETE FROM categoria;")
        cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('pessoa', 'categoria');")

