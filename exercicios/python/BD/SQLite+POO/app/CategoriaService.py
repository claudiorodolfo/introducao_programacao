"""
Serviço para interação do usuário via linha de comando com a entidade Categoria
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria


class CategoriaService:
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
        self.categoria_dao = CategoriaDAO(db)
    
    def exibir_menu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE CATEGORIAS")
        print("="*50)
        print("1. Criar categoria")
        print("2. Listar todas as categorias")
        print("3. Buscar categoria por ID")
        print("4. Buscar categoria por nome")
        print("5. Atualizar categoria")
        print("6. Deletar categoria")
        print("0. Sair")
        print("="*50)
    
    def criar_categoria(self):
        """Solicita dados do usuário e cria uma nova categoria"""
        print("\n--- CRIAR CATEGORIA ---")
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("❌ Erro: O nome da categoria não pode ser vazio!")
            return
        
        try:
            # Verificar se já existe uma categoria com esse nome
            categoria_existente = self.categoria_dao.buscarPorNome(nome)
            if categoria_existente:
                print(f"❌ Erro: Já existe uma categoria com o nome '{nome}' (ID: {categoria_existente.id})")
                return
            
            # Criar nova categoria
            categoria = Categoria(id=None, nome=nome)
            categoria_id = self.categoria_dao.salvar(categoria)
            print(f"✅ Categoria criada com sucesso!")
            print(f"   ID: {categoria_id}")
            print(f"   Nome: {categoria.nome}")
        
        except Exception as e:
            print(f"❌ Erro ao criar categoria: {e}")
            self.db.rollback()
    
    def listar_categorias(self):
        """Lista todas as categorias cadastradas"""
        print("\n--- LISTAR TODAS AS CATEGORIAS ---")
        
        try:
            categorias = self.categoria_dao.listarTodas()
            
            if not categorias:
                print("⚠️  Nenhuma categoria cadastrada.")
                return
            
            print(f"\nTotal de categorias: {len(categorias)}")
            print("\n" + "-"*50)
            print(f"{'ID':<5} | {'Nome':<30}")
            print("-"*50)
            
            for categoria in categorias:
                print(f"{categoria.id:<5} | {categoria.nome:<30}")
            
            print("-"*50)
        
        except Exception as e:
            print(f"❌ Erro ao listar categorias: {e}")
    
    def buscar_por_id(self):
        """Solicita um ID e busca a categoria correspondente"""
        print("\n--- BUSCAR CATEGORIA POR ID ---")
        
        try:
            id_str = input("Digite o ID da categoria: ").strip()
            categoria_id = int(id_str)
            
            categoria = self.categoria_dao.buscarPorId(categoria_id)
            
            if categoria:
                print("\n✅ Categoria encontrada:")
                print(f"   ID: {categoria.id}")
                print(f"   Nome: {categoria.nome}")
            else:
                print(f"⚠️  Categoria com ID {categoria_id} não encontrada.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar categoria: {e}")
    
    def buscar_por_nome(self):
        """Solicita um nome e busca a categoria correspondente"""
        print("\n--- BUSCAR CATEGORIA POR NOME ---")
        
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        try:
            categoria = self.categoria_dao.buscarPorNome(nome)
            
            if categoria:
                print("\n✅ Categoria encontrada:")
                print(f"   ID: {categoria.id}")
                print(f"   Nome: {categoria.nome}")
            else:
                print(f"⚠️  Categoria '{nome}' não encontrada.")
        
        except Exception as e:
            print(f"❌ Erro ao buscar categoria: {e}")
    
    def atualizar_categoria(self):
        """Solicita dados do usuário e atualiza uma categoria existente"""
        print("\n--- ATUALIZAR CATEGORIA ---")
        
        try:
            id_str = input("Digite o ID da categoria a atualizar: ").strip()
            categoria_id = int(id_str)
            
            # Buscar a categoria existente
            categoria = self.categoria_dao.buscarPorId(categoria_id)
            
            if not categoria:
                print(f"⚠️  Categoria com ID {categoria_id} não encontrada.")
                return
            
            print(f"\nCategoria atual:")
            print(f"   ID: {categoria.id}")
            print(f"   Nome: {categoria.nome}")
            
            novo_nome = input("\nDigite o novo nome da categoria (ou Enter para manter): ").strip()
            
            if not novo_nome:
                print("⚠️  Operação cancelada. Nome não foi alterado.")
                return
            
            # Verificar se já existe outra categoria com esse nome
            categoria_existente = self.categoria_dao.buscarPorNome(novo_nome)
            if categoria_existente and categoria_existente.id != categoria_id:
                print(f"❌ Erro: Já existe outra categoria com o nome '{novo_nome}' (ID: {categoria_existente.id})")
                return
            
            # Atualizar categoria
            categoria.nome = novo_nome
            self.categoria_dao.salvar(categoria)
            print(f"\n✅ Categoria atualizada com sucesso!")
            print(f"   ID: {categoria.id}")
            print(f"   Nome: {categoria.nome}")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao atualizar categoria: {e}")
            self.db.rollback()
    
    def deletar_categoria(self):
        """Solicita um ID e deleta a categoria correspondente"""
        print("\n--- DELETAR CATEGORIA ---")
        
        try:
            id_str = input("Digite o ID da categoria a deletar: ").strip()
            categoria_id = int(id_str)
            
            # Buscar a categoria existente
            categoria = self.categoria_dao.buscarPorId(categoria_id)
            
            if not categoria:
                print(f"⚠️  Categoria com ID {categoria_id} não encontrada.")
                return
            
            print(f"\nCategoria a ser deletada:")
            print(f"   ID: {categoria.id}")
            print(f"   Nome: {categoria.nome}")
            
            confirmacao = input("\n⚠️  Tem certeza que deseja deletar esta categoria? (s/N): ").strip().lower()
            
            if confirmacao != 's':
                print("❌ Operação cancelada.")
                return
            
            sucesso = self.categoria_dao.deletar(categoria)
            
            if sucesso:
                print(f"\n✅ Categoria deletada com sucesso!")
            else:
                print(f"\n❌ Erro ao deletar categoria.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao deletar categoria: {e}")
            self.db.rollback()
    
    def executar(self):
        """Método principal que executa o loop do menu"""
        try:
            while True:
                self.exibir_menu()
                opcao = input("\nEscolha uma opção: ").strip()
                
                if opcao == '0':
                    print("\n👋 Encerrando o sistema...")
                    break
                elif opcao == '1':
                    self.criar_categoria()
                elif opcao == '2':
                    self.listar_categorias()
                elif opcao == '3':
                    self.buscar_por_id()
                elif opcao == '4':
                    self.buscar_por_nome()
                elif opcao == '5':
                    self.atualizar_categoria()
                elif opcao == '6':
                    self.deletar_categoria()
                else:
                    print("❌ Opção inválida! Tente novamente.")
                
                input("\nPressione Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário.")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Função principal para executar o serviço"""
    db = DatabaseConnection('exemplo_bd.db')
    
    try:
        # Conectar ao banco
        db.conectar()
        
        # Garantir que as tabelas existam
        db.criarTabelas()
        
        # Criar e executar o serviço
        service = CategoriaService(db)
        service.executar()
    
    except Exception as e:
        print(f"❌ Erro ao inicializar o sistema: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.fechar()
        print("✓ Conexão com banco de dados encerrada.")


if __name__ == "__main__":
    main()

