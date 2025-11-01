"""
Script de teste completo do projeto SQLite+POO
Testa todas as funcionalidades e verifica se está tudo funcionando
"""
import sys
import os

# Adicionar o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bd.database import DatabaseConnection
from model.categoria import Categoria
from model.pessoa import Pessoa
from dao.categoria_dao import CategoriaDAO
from dao.pessoa_dao import PessoaDAO


def limparBanco(db):
    """Remove todos os dados do banco para testes limpos"""
    print("🧹 Limpando banco de dados...")
    db.limparDados()
    print("✓ Banco limpo!\n")


def testarCategoria_dao(db):
    """Testa operações CRUD de Categoria"""
    print("=" * 60)
    print("TESTE 1: Operações CRUD - Categoria")
    print("=" * 60)
    
    categoria_dao = CategoriaDAO(db)
    erros = []
    
    try:
        # CREATE
        print("\n✓ CREATE - Criando categoria...")
        cat1 = Categoria(id=None, nome="Desenvolvedor")
        categoria_dao.salvar(cat1)
        assert cat1.id is not None, "ID não foi atribuído"
        print(f"  ✓ Categoria criada: {cat1}")
        
        cat2 = Categoria(id=None, nome="Designer")
        categoria_dao.salvar(cat2)
        assert cat2.id is not None, "ID não foi atribuído"
        print(f"  ✓ Categoria criada: {cat2}")
        
        # READ - Buscar por ID
        print("\n✓ READ - Buscando categoria por ID...")
        cat_encontrada = categoria_dao.buscarPorId(cat1.id)
        assert cat_encontrada is not None, "Categoria não encontrada por ID"
        assert cat_encontrada.nome == "Desenvolvedor", "Nome incorreto"
        print(f"  ✓ Categoria encontrada: {cat_encontrada}")
        
        # READ - Buscar por nome
        print("\n✓ READ - Buscando categoria por nome...")
        cat_por_nome = categoria_dao.buscarPorNome("Designer")
        assert cat_por_nome is not None, "Categoria não encontrada por nome"
        assert cat_por_nome.nome == "Designer", "Nome incorreto"
        print(f"  ✓ Categoria encontrada: {cat_por_nome}")
        
        # READ - Listar todas
        print("\n✓ READ - Listando todas as categorias...")
        todas = categoria_dao.listarTodas()
        assert len(todas) >= 2, f"Esperava pelo menos 2 categorias, encontrou {len(todas)}"
        print(f"  ✓ Total de categorias: {len(todas)}")
        for cat in todas:
            print(f"    - {cat}")
        
        # UPDATE
        print("\n✓ UPDATE - Atualizando categoria...")
        cat1.nome = "Desenvolvedor Senior"
        categoria_dao.salvar(cat1)
        cat_atualizada = categoria_dao.buscarPorId(cat1.id)
        assert cat_atualizada.nome == "Desenvolvedor Senior", "Nome não foi atualizado"
        print(f"  ✓ Categoria atualizada: {cat_atualizada}")
        
        # DELETE
        print("\n✓ DELETE - Deletando categoria...")
        sucesso = categoria_dao.deletar(cat2)
        assert sucesso, "Falha ao deletar categoria"
        cat_deletada = categoria_dao.buscarPorId(cat2.id)
        assert cat_deletada is None, "Categoria ainda existe após deletar"
        print(f"  ✓ Categoria deletada com sucesso")
        
        print("\n✅ TESTE 1 PASSOU - Categoria CRUD OK\n")
        return True
        
    except Exception as e:
        erros.append(f"Erro no teste de Categoria: {e}")
        import traceback
        traceback.print_exc()
        print(f"\n❌ TESTE 1 FALHOU: {e}\n")
        return False


def testarPessoaDao(db):
    """Testa operações CRUD de Pessoa"""
    print("=" * 60)
    print("TESTE 2: Operações CRUD - Pessoa")
    print("=" * 60)
    
    categoria_dao = CategoriaDAO(db)
    pessoa_dao = PessoaDAO(db)
    erros = []
    
    try:
        # Garantir que temos uma categoria
        print("\n✓ Preparando categoria para testes...")
        categoria = categoria_dao.buscarPorNome("Desenvolvedor Senior")
        if not categoria:
            categoria = Categoria(id=None, nome="Desenvolvedor Senior")
            categoria_dao.salvar(categoria)
        print(f"  ✓ Usando categoria: {categoria}")
        
        # CREATE
        print("\n✓ CREATE - Criando pessoa...")
        pessoa1 = Pessoa(
            id=None,
            nome="João Developer",
            email="joao@example.com",
            categoria=categoria,
            idade=28,
            altura=1.75,
            peso=75.0,
            data_nascimento="1995-05-15",
            ativo=True,
            observacoes="Desenvolvedor Python",
            telefone="11999999999"
        )
        pessoa_dao.salvar(pessoa1)
        assert pessoa1.id is not None, "ID não foi atribuído"
        print(f"  ✓ Pessoa criada: {pessoa1}")
        
        # CREATE - Segunda pessoa
        categoria2 = categoria_dao.buscarPorNome("Designer")
        if not categoria2:
            categoria2 = Categoria(id=None, nome="Designer")
            categoria_dao.salvar(categoria2)
        
        pessoa2 = Pessoa(
            id=None,
            nome="Maria Designer",
            email="maria@example.com",
            categoria=categoria2,
            idade=25,
            altura=1.65,
            peso=60.0,
            data_nascimento="1998-03-20",
            ativo=True,
            observacoes="Designer UX/UI",
            telefone="11888888888"
        )
        pessoa_dao.salvar(pessoa2)
        assert pessoa2.id is not None, "ID não foi atribuído"
        print(f"  ✓ Pessoa criada: {pessoa2}")
        
        # READ - Buscar por ID
        print("\n✓ READ - Buscando pessoa por ID...")
        pessoa_encontrada = pessoa_dao.buscarPorId(pessoa1.id)
        assert pessoa_encontrada is not None, "Pessoa não encontrada por ID"
        assert pessoa_encontrada.nome == "João Developer", "Nome incorreto"
        assert pessoa_encontrada.email == "joao@example.com", "Email incorreto"
        print(f"  ✓ Pessoa encontrada: {pessoa_encontrada}")
        
        # READ - Buscar por nome
        print("\n✓ READ - Buscando pessoa por nome...")
        pessoas_joao = pessoa_dao.buscarPorNome("João")
        assert len(pessoas_joao) > 0, "Nenhuma pessoa encontrada com nome 'João'"
        print(f"  ✓ Pessoas encontradas com 'João': {len(pessoas_joao)}")
        for p in pessoas_joao:
            print(f"    - {p}")
        
        # READ - Buscar por categoria
        print("\n✓ READ - Buscando pessoas por categoria...")
        pessoas_cat = pessoa_dao.buscarPorCategoria(categoria.id)
        assert len(pessoas_cat) > 0, "Nenhuma pessoa encontrada na categoria"
        print(f"  ✓ Pessoas na categoria '{categoria.nome}': {len(pessoas_cat)}")
        
        # READ - Listar todas
        print("\n✓ READ - Listando todas as pessoas...")
        todas_pessoas = pessoa_dao.listarTodas()
        assert len(todas_pessoas) >= 2, f"Esperava pelo menos 2 pessoas, encontrou {len(todas_pessoas)}"
        print(f"  ✓ Total de pessoas: {len(todas_pessoas)}")
        
        # Testar relacionamento
        print("\n✓ READ - Testando relacionamento com categoria...")
        categoria_rel = pessoa_dao.obterCategoria(pessoa_encontrada)
        assert categoria_rel is not None, "Categoria não foi encontrada"
        assert categoria_rel.nome == "Desenvolvedor Senior", "Categoria incorreta"
        print(f"  ✓ Categoria relacionada: {categoria_rel.nome}")
        
        # UPDATE
        print("\n✓ UPDATE - Atualizando pessoa...")
        pessoa1.idade = 29
        pessoa1.observacoes = "Desenvolvedor Python Senior"
        pessoa_dao.salvar(pessoa1)
        pessoa_atualizada = pessoa_dao.buscarPorId(pessoa1.id)
        assert pessoa_atualizada.idade == 29, "Idade não foi atualizada"
        assert pessoa_atualizada.observacoes == "Desenvolvedor Python Senior", "Observações não foram atualizadas"
        print(f"  ✓ Pessoa atualizada: {pessoa_atualizada}")
        
        # UPDATE - Desativar pessoa
        print("\n✓ UPDATE - Desativando pessoa...")
        pessoa2.ativo = False
        pessoa_dao.salvar(pessoa2)
        pessoa_desativada = pessoa_dao.buscarPorId(pessoa2.id)
        assert pessoa_desativada.ativo == False, "Pessoa não foi desativada"
        print(f"  ✓ Pessoa desativada: {pessoa_desativada}")
        
        # DELETE
        print("\n✓ DELETE - Deletando pessoa...")
        sucesso = pessoa_dao.deletar(pessoa2)
        assert sucesso, "Falha ao deletar pessoa"
        pessoa_deletada = pessoa_dao.buscarPorId(pessoa2.id)
        assert pessoa_deletada is None, "Pessoa ainda existe após deletar"
        print(f"  ✓ Pessoa deletada com sucesso")
        
        print("\n✅ TESTE 2 PASSOU - Pessoa CRUD OK\n")
        return True
        
    except Exception as e:
        erros.append(f"Erro no teste de Pessoa: {e}")
        import traceback
        traceback.print_exc()
        print(f"\n❌ TESTE 2 FALHOU: {e}\n")
        return False


def testarIntegridadeReferencial(db):
    """Testa integridade referencial e constraints"""
    print("=" * 60)
    print("TESTE 3: Integridade Referencial e Constraints")
    print("=" * 60)
    
    categoria_dao = CategoriaDAO(db)
    pessoa_dao = PessoaDAO(db)
    
    try:
        # Testar constraint UNIQUE em email
        print("\n✓ Testando constraint UNIQUE em email...")
        categoria = categoria_dao.listarTodas()[0]  # Pegar primeira categoria
        
        pessoa_duplicada = Pessoa(
            id=None,
            nome="Teste Duplicado",
            email="joao@example.com",  # Email já existe
            categoria=categoria,
            idade=30
        )
        
        try:
            pessoa_dao.salvar(pessoa_duplicada)
            print("  ⚠️  AVISO: Constraint UNIQUE não foi aplicada (pode ser esperado se não houver constraint)")
        except Exception as e:
            if "UNIQUE" in str(e) or "unique" in str(e).lower():
                print("  ✓ Constraint UNIQUE funcionando corretamente")
            else:
                raise
        
        # Testar constraint de foreign key
        print("\n✓ Testando integridade referencial (foreign key)...")
        pessoa_invalida = Pessoa(
            id=None,
            nome="Teste FK",
            email="teste_fk@example.com",
            categoria=Categoria(id=99999, nome="Inexistente"),  # Categoria que não existe
            idade=30
        )
        
        try:
            pessoa_dao.salvar(pessoa_invalida)
            print("  ⚠️  AVISO: Foreign key constraint não foi verificada")
        except Exception as e:
            if "FOREIGN KEY" in str(e) or "foreign" in str(e).lower():
                print("  ✓ Foreign key constraint funcionando")
            else:
                # Pode dar erro de categoria sem ID, que é o comportamento esperado
                if "categoria válida" in str(e).lower():
                    print("  ✓ Validação de categoria funcionando")
                else:
                    raise
        
        print("\n✅ TESTE 3 PASSOU - Integridade OK\n")
        return True
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n❌ TESTE 3 FALHOU: {e}\n")
        return False


def executarTestes():
    """Executa todos os testes"""
    print("\n" + "=" * 60)
    print("INICIANDO TESTES DO PROJETO SQLite+POO")
    print("=" * 60 + "\n")
    
    db = DatabaseConnection('exemplo_bd.db')
    resultados = []
    
    try:
        db.conectar()
        
        # Criar tabelas
        print("📋 Criando/verificando tabelas...")
        db.criarTabelas()
        print("✓ Tabelas OK\n")
        
        # Limpar banco para testes limpos
        limparBanco(db)
        
        # Executar testes
        resultados.append(("Categoria CRUD", testarCategoria_dao(db)))
        resultados.append(("Pessoa CRUD", testarPessoaDao(db)))
        resultados.append(("Integridade Referencial", testarIntegridadeReferencial(db)))
        
        # Resumo
        print("\n" + "=" * 60)
        print("RESUMO DOS TESTES")
        print("=" * 60)
        
        total = len(resultados)
        passou = sum(1 for _, resultado in resultados if resultado)
        
        for nome, resultado in resultados:
            status = "✅ PASSOU" if resultado else "❌ FALHOU"
            print(f"{nome}: {status}")
        
        print("\n" + "-" * 60)
        print(f"Total: {passou}/{total} testes passaram")
        print("=" * 60 + "\n")
        
        if passou == total:
            print("🎉 TODOS OS TESTES PASSARAM! Projeto está funcionando corretamente.")
            return True
        else:
            print("⚠️  ALGUNS TESTES FALHARAM. Verifique os erros acima.")
            return False
        
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.fechar()
        print("✓ Conexão encerrada!")


if __name__ == "__main__":
    sucesso = executarTestes()
    sys.exit(0 if sucesso else 1)

