"""
Exemplo de uso das classes ORM para demonstrar operações CRUD
"""
from bd.database import DatabaseConnection
from model.categoria import Categoria
from model.pessoa import Pessoa
from dao.categoria_dao import CategoriaDAO
from dao.pessoa_dao import PessoaDAO


def exemploCrudCompleto():   # Criar conexão
    db = DatabaseConnection('exemplo_bd.db')
    
    try:
        db.conectar()
        
        # Criar tabelas se não existirem
        db.criarTabelas()
        
        # Criar instâncias dos DAOs
        pessoa_dao = PessoaDAO(db)
        categoria_dao = CategoriaDAO(db)
        
        # ===== CREATE (Criar) =====
        print("=== CREATE - Criando registros ===")
        
        # Criar categorias (verificar se já existem primeiro)
        cat1 = categoria_dao.buscarPorNome("Desenvolvedor")
        if not cat1:
            cat1 = Categoria(id=None, nome="Desenvolvedor")
            categoria_dao.salvar(cat1)
            print(f"Categoria criada: {cat1}")
        else:
            print(f"Categoria já existe: {cat1}")
        
        cat2 = categoria_dao.buscarPorNome("Designer")
        if not cat2:
            cat2 = Categoria(id=None, nome="Designer")
            categoria_dao.salvar(cat2)
            print(f"Categoria criada: {cat2}")
        else:
            print(f"Categoria já existe: {cat2}")
        
        # Criar pessoas (verificar se já existem por email)
        pessoas_joao = pessoa_dao.buscarPorNome("João Developer")
        if pessoas_joao and any(p.email == "joao@example.com" for p in pessoas_joao):
            pessoa1 = next(p for p in pessoas_joao if p.email == "joao@example.com")
            print(f"Pessoa já existe: {pessoa1}")
        else:
            pessoa1 = Pessoa(
                id=None,
                nome="João Developer",
                email="joao@example.com",
                categoria=cat1,
                idade=28,
                altura=1.75,
                peso=75.0,
                data_nascimento="1995-05-15",
                ativo=True,
                observacoes="Desenvolvedor Python",
                telefone="11999999999"
            )
            pessoa_dao.salvar(pessoa1)
            print(f"Pessoa criada: {pessoa1}")
        
        pessoas_maria = pessoa_dao.buscarPorNome("Maria Designer")
        if pessoas_maria and any(p.email == "maria@example.com" for p in pessoas_maria):
            pessoa2 = next(p for p in pessoas_maria if p.email == "maria@example.com")
            print(f"Pessoa já existe: {pessoa2}")
        else:
            pessoa2 = Pessoa(
                id=None,
                nome="Maria Designer",
                email="maria@example.com",
                categoria=cat2,
                idade=25,
                altura=1.65,
                peso=60.0,
                data_nascimento="1998-03-20",
                ativo=True,
                observacoes="Designer UX/UI",
                telefone="11888888888"
            )
            pessoa_dao.salvar(pessoa2)
            print(f"Pessoa criada: {pessoa2}")
        print()
        
        # ===== READ (Ler) =====
        print("=== READ - Lendo registros ===")
        
        # Buscar por ID
        categoria_encontrada = categoria_dao.buscarPorId(cat1.id)
        print(f"Categoria encontrada por ID: {categoria_encontrada}")
        
        # Buscar por nome
        categoria_por_nome = categoria_dao.buscarPorNome("Designer")
        print(f"Categoria encontrada por nome: {categoria_por_nome}")
        
        # Listar todas
        todas_categorias = categoria_dao.listarTodas()
        print(f"\nTodas as categorias ({len(todas_categorias)}):")
        for cat in todas_categorias:
            print(f"  - {cat}")
        
        # Buscar pessoas por nome
        pessoas_encontradas = pessoa_dao.buscarPorNome("João")
        print(f"\nPessoas encontradas com 'João' ({len(pessoas_encontradas)}):")
        for p in pessoas_encontradas:
            print(f"  - {p}")
        
        # Buscar pessoas por categoria
        devs = pessoa_dao.buscarPorCategoria(cat1.id)
        print(f"\nPessoas da categoria 'Desenvolvedor' ({len(devs)}):")
        for p in devs:
            categoria = pessoa_dao.obterCategoria(p)
            print(f"  - {p.nome} ({categoria.nome if categoria else 'N/A'})")
        
        # ===== UPDATE (Atualizar) =====
        print("\n=== UPDATE - Atualizando registros ===")
        
        # Atualizar categoria (verificar se nome já existe)
        novo_nome = "Desenvolvedor Senior"
        cat_existente = categoria_dao.buscarPorNome(novo_nome)
        if cat_existente and cat_existente.id != cat1.id:
            print(f"Categoria '{novo_nome}' já existe com outro ID. Usando a existente.")
            cat1 = cat_existente
        else:
            cat1.nome = novo_nome
            categoria_dao.salvar(cat1)
        print(f"Categoria: {cat1}")
        
        # Atualizar pessoa
        pessoa1.idade = 29
        pessoa1.observacoes = "Desenvolvedor Python Senior"
        pessoa_dao.salvar(pessoa1)
        print(f"Pessoa atualizada: {pessoa1}")
        
        # Desativar pessoa
        pessoa2.ativo = False
        pessoa_dao.salvar(pessoa2)
        print(f"Pessoa desativada: {pessoa2}")
        
        # ===== DELETE (Deletar) =====
        print("\n=== DELETE - Deletando registros ===")
        
        # Deletar pessoa (deve deletar antes de categoria se houver FK)
        pessoa2_deletada = pessoa_dao.deletar(pessoa2)
        print(f"Pessoa deletada: {pessoa2_deletada}")
        
        # Verificar se foi deletada
        pessoa_verificada = pessoa_dao.buscarPorId(pessoa2.id)
        print(f"Pessoa ainda existe? {pessoa_verificada is not None}")
        
        # ===== Relacionamentos =====
        print("\n=== RELACIONAMENTOS ===")
        
        pessoa1_atualizada = pessoa_dao.buscarPorId(pessoa1.id)
        if pessoa1_atualizada:
            categoria_relacionada = pessoa_dao.obterCategoria(pessoa1_atualizada)
            print(f"Pessoa: {pessoa1_atualizada.nome}")
            print(f"Categoria relacionada: {categoria_relacionada.nome if categoria_relacionada else 'N/A'}")
        
    except Exception as e:
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.fechar()
        print("\n✓ Conexão encerrada!")


if __name__ == "__main__":
    exemploCrudCompleto()

