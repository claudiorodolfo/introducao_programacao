# Classe que representa um carro estacionado
class Carro:
    def __init__(self, placa, posicao, tamanho):
        self.posicao = posicao
        self.tamanho = tamanho
        self.placa = placa

    def __repr__(self):
        return "posicao: %s tamanho: %s placa: %s" % (self.posicao, self.tamanho, self.placa)

    def get_posicao(self):
        return self.posicao

    def get_tamanho(self):
        return self.tamanho

    def get_placa(self):
        return self.placa



# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
while True:
    try:

        index = 0
        tamanho_ocupado = 0
        resposta = ""
        valor_recebido = 0
        lista_carros = []

        tamanho_estacionamento, quantidade_eventos = input().split()
        # Recolhendo o tamanho do estacionamento e a quantidade de eventos

        tamanho_estacionamento = int(tamanho_estacionamento)
        quantidade_eventos = int(quantidade_eventos)

        for i in range(quantidade_eventos):
            lista_argumentos = input().split()
            tipo_evento = lista_argumentos[0]
            placa = lista_argumentos[1]
            if(tipo_evento == "C"):
                tamanho_veiculo = int(lista_argumentos[2])
                # Se não existe nenhum carro estacionado, e o estacionamento suporta o carro, ele é inserido no início da lista
                if(len(lista_carros) == 0):
                    if (tamanho_veiculo <= tamanho_estacionamento):
                        carro = Carro(placa, 0, tamanho_veiculo)
                        lista_carros.insert(0,carro)
                        valor_recebido += 10
                else:
                    ultima_posicao = 0
                    disponibilidade = 0
                    index_novo_carro = 0
                    for carro in lista_carros:
                        index_novo_carro += 1
                        # Caso o carro esteja imediatamente depois da última posição, então não há nenhum espaço disponível entre
                        # a última posição e este carro
                        if(carro.posicao == ultima_posicao):
                            # Calculando a próxima posição para inserir carros
                            ultima_posicao = carro.posicao + carro.tamanho
                            # Disponibilidade que está disponível no fim do estacionamento
                            disponibilidade = tamanho_estacionamento - ultima_posicao
                        else:
                            # Calculando espaço entre a última posição de um carro e este carro
                            disponibilidade = carro.posicao - ultima_posicao
                            # Se o espaço entre eles for suficiente, o carro é inserido no estacionamento
                            if(disponibilidade >= tamanho_veiculo):
                                index_novo_carro -= 1
                                break
                            else:
                                # Definindo a ultima posição após o carro
                                ultima_posicao = carro.posicao + carro.tamanho
                                disponibilidade = tamanho_estacionamento - ultima_posicao
        
        
                    # Adicionando o carro caso exista espaço disponível
                    if (disponibilidade >= tamanho_veiculo):
                        carro = Carro(placa, ultima_posicao, tamanho_veiculo)
                        lista_carros.insert(index_novo_carro, carro)
                        valor_recebido += 10
            elif(tipo_evento == "S"):
                # Removendo o carro da lista
                index_lista = 0
                for carro in lista_carros:
                    if(carro.placa == placa):
                        break
                    index_lista += 1
                del lista_carros[index_lista]
        
            index += 1
        
        print(valor_recebido)
    except EOFError:
        break

