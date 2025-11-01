"""
Serviço para interação do usuário via linha de comando com a entidade Pessoa
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from dao.pessoa_dao import PessoaDAO
from dao.categoria_dao import CategoriaDAO
from model.pessoa import Pessoa
from model.categoria import Categoria


class PessoaService:
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
        self.pessoa_dao = PessoaDAO(db)
        self.categoria_dao = CategoriaDAO(db)
    
    def exibir_menu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE PESSOAS")
        print("="*50)
        print("1. Criar pessoa")
        print("2. Listar todas as pessoas")
        print("3. Buscar pessoa por ID")
        print("4. Buscar pessoa por nome")
        print("5. Buscar pessoas por categoria")
        print("6. Atualizar pessoa")
        print("7. Deletar pessoa")
        print("0. Sair")
        print("="*50)
    
    def listar_categorias_disponiveis(self):
        """Lista todas as categorias disponíveis para seleção"""
        categorias = self.categoria_dao.listarTodas()
        if not categorias:
            print("⚠️  Nenhuma categoria cadastrada. Cadastre uma categoria primeiro!")
            return None
        
        print("\nCategorias disponíveis:")
        print("-"*30)
        for cat in categorias:
            print(f"  {cat.id}. {cat.nome}")
        print("-"*30)
        return categorias
    
    def selecionar_categoria(self):
        """Solicita ao usuário que selecione uma categoria"""
        categorias = self.listar_categorias_disponiveis()
        if not categorias:
            return None
        
        try:
            categoria_id_str = input("Digite o ID da categoria: ").strip()
            categoria_id = int(categoria_id_str)
            
            categoria = self.categoria_dao.buscarPorId(categoria_id)
            if not categoria:
                print(f"❌ Erro: Categoria com ID {categoria_id} não encontrada!")
                return None
            
            return categoria
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
            return None
    
    def criar_pessoa(self):
        """Solicita dados do usuário e cria uma nova pessoa"""
        print("\n--- CRIAR PESSOA ---")
        
        nome = input("Digite o nome: ").strip()
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        email = input("Digite o email: ").strip()
        if not email:
            print("❌ Erro: O email não pode ser vazio!")
            return
        
        # Verificar se já existe uma pessoa com esse email
        pessoas_existentes = self.pessoa_dao.buscarPorNome("")  # Buscar todas para verificar email
        todas_pessoas = self.pessoa_dao.listarTodas()
        for p in todas_pessoas:
            if p.email.lower() == email.lower():
                print(f"❌ Erro: Já existe uma pessoa com o email '{email}' (ID: {p.id})")
                return
        
        # Selecionar categoria
        categoria = self.selecionar_categoria()
        if not categoria:
            return
        
        # Campos opcionais
        idade_str = input("Digite a idade (ou Enter para pular): ").strip()
        idade = int(idade_str) if idade_str else None
        
        altura_str = input("Digite a altura em metros (ex: 1.75, ou Enter para pular): ").strip()
        altura = float(altura_str) if altura_str else None
        
        peso_str = input("Digite o peso em kg (ex: 75.5, ou Enter para pular): ").strip()
        peso = float(peso_str) if peso_str else None
        
        data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD, ou Enter para pular): ").strip()
        data_nascimento = data_nascimento if data_nascimento else None
        
        telefone = input("Digite o telefone (ou Enter para pular): ").strip()
        telefone = telefone if telefone else None
        
        observacoes = input("Digite observações (ou Enter para pular): ").strip()
        observacoes = observacoes if observacoes else None
        
        ativo_str = input("Pessoa está ativa? (S/n): ").strip().lower()
        ativo = ativo_str != 'n'
        
        try:
            pessoa = Pessoa(
                id=None,
                nome=nome,
                email=email,
                categoria=categoria,
                idade=idade,
                altura=altura,
                peso=peso,
                data_nascimento=data_nascimento,
                ativo=ativo,
                observacoes=observacoes,
                telefone=telefone
            )
            
            pessoa_id = self.pessoa_dao.salvar(pessoa)
            print(f"\n✅ Pessoa criada com sucesso!")
            self.exibir_detalhes_pessoa(pessoa)
        
        except ValueError as e:
            print(f"❌ Erro de validação: {e}")
            self.db.rollback()
        except Exception as e:
            print(f"❌ Erro ao criar pessoa: {e}")
            self.db.rollback()
    
    def exibir_detalhes_pessoa(self, pessoa: Pessoa):
        """Exibe os detalhes completos de uma pessoa"""
        print(f"\n   ID: {pessoa.id}")
        print(f"   Nome: {pessoa.nome}")
        print(f"   Email: {pessoa.email}")
        print(f"   Categoria: {pessoa.categoria.nome} (ID: {pessoa.categoria.id})")
        if pessoa.idade is not None:
            print(f"   Idade: {pessoa.idade} anos")
        if pessoa.altura is not None:
            print(f"   Altura: {pessoa.altura}m")
        if pessoa.peso is not None:
            print(f"   Peso: {pessoa.peso}kg")
        if pessoa.data_nascimento:
            print(f"   Data de nascimento: {pessoa.data_nascimento}")
        if pessoa.telefone:
            print(f"   Telefone: {pessoa.telefone}")
        print(f"   Status: {'✅ Ativa' if pessoa.ativo else '❌ Inativa'}")
        if pessoa.observacoes:
            print(f"   Observações: {pessoa.observacoes}")
        if pessoa.momento_cadastro:
            print(f"   Cadastrado em: {pessoa.momento_cadastro}")
    
    def listar_pessoas(self):
        """Lista todas as pessoas cadastradas"""
        print("\n--- LISTAR TODAS AS PESSOAS ---")
        
        try:
            pessoas = self.pessoa_dao.listarTodas()
            
            if not pessoas:
                print("⚠️  Nenhuma pessoa cadastrada.")
                return
            
            print(f"\nTotal de pessoas: {len(pessoas)}")
            print("\n" + "-"*80)
            print(f"{'ID':<5} | {'Nome':<25} | {'Email':<25} | {'Categoria':<15} | {'Status':<8}")
            print("-"*80)
            
            for pessoa in pessoas:
                status = "Ativa" if pessoa.ativo else "Inativa"
                print(f"{pessoa.id:<5} | {pessoa.nome[:24]:<25} | {pessoa.email[:24]:<25} | {pessoa.categoria.nome[:14]:<15} | {status:<8}")
            
            print("-"*80)
        
        except Exception as e:
            print(f"❌ Erro ao listar pessoas: {e}")
    
    def buscar_por_id(self):
        """Solicita um ID e busca a pessoa correspondente"""
        print("\n--- BUSCAR PESSOA POR ID ---")
        
        try:
            id_str = input("Digite o ID da pessoa: ").strip()
            pessoa_id = int(id_str)
            
            pessoa = self.pessoa_dao.buscarPorId(pessoa_id)
            
            if pessoa:
                print("\n✅ Pessoa encontrada:")
                self.exibir_detalhes_pessoa(pessoa)
            else:
                print(f"⚠️  Pessoa com ID {pessoa_id} não encontrada.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar pessoa: {e}")
    
    def buscar_por_nome(self):
        """Solicita um nome e busca pessoas correspondentes"""
        print("\n--- BUSCAR PESSOA POR NOME ---")
        
        nome = input("Digite o nome (ou parte do nome) da pessoa: ").strip()
        
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        try:
            pessoas = self.pessoa_dao.buscarPorNome(nome)
            
            if pessoas:
                print(f"\n✅ {len(pessoas)} pessoa(s) encontrada(s):")
                print("\n" + "-"*80)
                for pessoa in pessoas:
                    print(f"ID: {pessoa.id} | {pessoa.nome} | {pessoa.email} | {pessoa.categoria.nome}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma pessoa encontrada com o nome contendo '{nome}'.")
        
        except Exception as e:
            print(f"❌ Erro ao buscar pessoa: {e}")
    
    def buscar_por_categoria(self):
        """Lista pessoas de uma categoria específica"""
        print("\n--- BUSCAR PESSOAS POR CATEGORIA ---")
        
        categorias = self.listar_categorias_disponiveis()
        if not categorias:
            return
        
        try:
            categoria_id_str = input("Digite o ID da categoria: ").strip()
            categoria_id = int(categoria_id_str)
            
            categoria = self.categoria_dao.buscarPorId(categoria_id)
            if not categoria:
                print(f"❌ Erro: Categoria com ID {categoria_id} não encontrada!")
                return
            
            pessoas = self.pessoa_dao.buscarPorCategoria(categoria_id)
            
            if pessoas:
                print(f"\n✅ {len(pessoas)} pessoa(s) encontrada(s) na categoria '{categoria.nome}':")
                print("\n" + "-"*80)
                for pessoa in pessoas:
                    status = "Ativa" if pessoa.ativo else "Inativa"
                    print(f"ID: {pessoa.id} | {pessoa.nome} | {pessoa.email} | Status: {status}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma pessoa encontrada na categoria '{categoria.nome}'.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar pessoas: {e}")
    
    def atualizar_pessoa(self):
        """Solicita dados do usuário e atualiza uma pessoa existente"""
        print("\n--- ATUALIZAR PESSOA ---")
        
        try:
            id_str = input("Digite o ID da pessoa a atualizar: ").strip()
            pessoa_id = int(id_str)
            
            pessoa = self.pessoa_dao.buscarPorId(pessoa_id)
            
            if not pessoa:
                print(f"⚠️  Pessoa com ID {pessoa_id} não encontrada.")
                return
            
            print(f"\nPessoa atual:")
            self.exibir_detalhes_pessoa(pessoa)
            
            print("\nDigite os novos dados (ou Enter para manter o valor atual):")
            
            # Nome
            novo_nome = input(f"Nome [{pessoa.nome}]: ").strip()
            if novo_nome:
                pessoa.nome = novo_nome
            
            # Email
            novo_email = input(f"Email [{pessoa.email}]: ").strip()
            if novo_email:
                # Verificar se já existe outra pessoa com esse email
                todas_pessoas = self.pessoa_dao.listarTodas()
                for p in todas_pessoas:
                    if p.id != pessoa_id and p.email.lower() == novo_email.lower():
                        print(f"❌ Erro: Já existe outra pessoa com o email '{novo_email}' (ID: {p.id})")
                        return
                pessoa.email = novo_email
            
            # Categoria
            categoria_str = input(f"Categoria ID [{pessoa.categoria.id} - {pessoa.categoria.nome}] (ou Enter para manter): ").strip()
            if categoria_str:
                nova_categoria_id = int(categoria_str)
                nova_categoria = self.categoria_dao.buscarPorId(nova_categoria_id)
                if not nova_categoria:
                    print(f"❌ Erro: Categoria com ID {nova_categoria_id} não encontrada!")
                    return
                pessoa.categoria = nova_categoria
            
            # Idade
            idade_str = input(f"Idade [{pessoa.idade or 'N/A'}] (ou Enter para manter): ").strip()
            if idade_str:
                pessoa.idade = int(idade_str) if idade_str else None
            elif not idade_str and pessoa.idade is not None:
                # Manter o valor atual
                pass
            
            # Altura
            altura_str = input(f"Altura [{pessoa.altura or 'N/A'}]m (ou Enter para manter): ").strip()
            if altura_str:
                pessoa.altura = float(altura_str) if altura_str else None
            
            # Peso
            peso_str = input(f"Peso [{pessoa.peso or 'N/A'}]kg (ou Enter para manter): ").strip()
            if peso_str:
                pessoa.peso = float(peso_str) if peso_str else None
            
            # Data de nascimento
            data_str = input(f"Data de nascimento [{pessoa.data_nascimento or 'N/A'}] (ou Enter para manter): ").strip()
            if data_str:
                pessoa.data_nascimento = data_str if data_str else None
            
            # Telefone
            telefone_str = input(f"Telefone [{pessoa.telefone or 'N/A'}] (ou Enter para manter): ").strip()
            if telefone_str:
                pessoa.telefone = telefone_str if telefone_str else None
            
            # Observações
            obs_str = input(f"Observações [{pessoa.observacoes or 'N/A'}] (ou Enter para manter): ").strip()
            if obs_str:
                pessoa.observacoes = obs_str if obs_str else None
            
            # Status ativo
            ativo_str = input(f"Status ativo (S/n) [{'S' if pessoa.ativo else 'n'}] (ou Enter para manter): ").strip().lower()
            if ativo_str:
                pessoa.ativo = ativo_str != 'n'
            
            self.pessoa_dao.salvar(pessoa)
            print(f"\n✅ Pessoa atualizada com sucesso!")
            print("\nDados atualizados:")
            self.exibir_detalhes_pessoa(pessoa)
        
        except ValueError as e:
            print(f"❌ Erro: {e}")
        except Exception as e:
            print(f"❌ Erro ao atualizar pessoa: {e}")
            self.db.rollback()
    
    def deletar_pessoa(self):
        """Solicita um ID e deleta a pessoa correspondente"""
        print("\n--- DELETAR PESSOA ---")
        
        try:
            id_str = input("Digite o ID da pessoa a deletar: ").strip()
            pessoa_id = int(id_str)
            
            pessoa = self.pessoa_dao.buscarPorId(pessoa_id)
            
            if not pessoa:
                print(f"⚠️  Pessoa com ID {pessoa_id} não encontrada.")
                return
            
            print(f"\nPessoa a ser deletada:")
            self.exibir_detalhes_pessoa(pessoa)
            
            confirmacao = input("\n⚠️  Tem certeza que deseja deletar esta pessoa? (s/N): ").strip().lower()
            
            if confirmacao != 's':
                print("❌ Operação cancelada.")
                return
            
            sucesso = self.pessoa_dao.deletar(pessoa)
            
            if sucesso:
                print(f"\n✅ Pessoa deletada com sucesso!")
            else:
                print(f"\n❌ Erro ao deletar pessoa.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao deletar pessoa: {e}")
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
                    self.criar_pessoa()
                elif opcao == '2':
                    self.listar_pessoas()
                elif opcao == '3':
                    self.buscar_por_id()
                elif opcao == '4':
                    self.buscar_por_nome()
                elif opcao == '5':
                    self.buscar_por_categoria()
                elif opcao == '6':
                    self.atualizar_pessoa()
                elif opcao == '7':
                    self.deletar_pessoa()
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
        service = PessoaService(db)
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

