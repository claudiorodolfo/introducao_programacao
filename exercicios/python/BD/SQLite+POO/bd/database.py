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
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn
    
    def fechar(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def commit(self):
        """Confirma as transações pendentes"""
        if self.conn:
            self.conn.commit()
    
    def rollback(self):
        """Desfaz as transações pendentes"""
        if self.conn:
            self.conn.rollback()
    
    def cursor(self):
        """Retorna um cursor para executar queries"""
        if self.conn is None:
            self.conectar()
        return self.conn.cursor()
    
    def criarTabelas(self):
        """Cria todas as tabelas necessárias"""
        # Importar aqui para evitar circular imports
        from dao.categoria_dao import CategoriaDAO
        from dao.pessoa_dao import PessoaDAO
        
        # Tabela categoria
        categoria_dao = CategoriaDAO(self)
        categoria_dao.criarTabela()
        
        # Tabela pessoa
        pessoa_dao = PessoaDAO(self)
        pessoa_dao.criarTabela()
    
    def limparDados(self):
        """Remove todos os dados das tabelas"""
        cur = self.cursor()
        cur.execute("DELETE FROM pessoa;")
        cur.execute("DELETE FROM categoria;")
        cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('pessoa', 'categoria');")
        self.commit()

