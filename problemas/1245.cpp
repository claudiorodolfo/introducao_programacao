//Problema 1245 - Botas Perdidas
//https://www.urionlinejudge.com.br/judge/pt/problems/view/1245
/*
A divisão de Suprimentos de Botas e Calçados do Exército comprou um grande número de pares de botas de vários tamanhos para seus soldados. No entanto, por uma falha de empacotamento da fábrica contratada, nem todas as caixas entregues continham um par de botas correto, com duas botas do mesmo tamanho, uma para cada pé. O sargento mandou que os recrutas retirassem todas as botas de todas as caixas para reembalá-las, desta vez corretamente.
Quando o sargento descobriu que você sabia programar, ele solicitou com a gentileza habitual que você escrevesse um programa que, dada a lista contendo a descrição de cada bota entregue, determina quantos pares corretos de botas poderão ser formados no total.

Entrada
A entrada é composta por diversos casos de teste e termina com final de arquivo (EOF). A primeira linha de um caso de teste contém um inteiro N (2 = N = 10 4), N é par, indicando o número de botas individuais entregues. Cada uma das N linhas seguintes descreve uma bota, contendo um número inteiro M (30 = M = 60) e uma letra L, separados por uma espaço em branco. M indica o número da bota e L indica o pé da bota: L = 'D' indica que a bota é para o pé direito, L = 'E' indica que a bota é para o pé esquerdo.

Saída
Para cada caso de teste imprima uma linha contendo um único número inteiro indicando o número total de pares corretos que podem ser formados.
*/
#include <iostream>

using namespace std;

int main() {
	
	int quantidade;
	bool continua = cin>>quantidade;

	while (continua) {
		
		bool bota_selecionada[quantidade];
		int bota_tamanho[quantidade];
		char bota_lado[quantidade];
		int total_pares = 0;
		
		//preenche os arrays com os dados fornecidos
		for (int i = 0; i < quantidade; i++) {
			cin>>bota_tamanho[i]>>bota_lado[i];
			bota_selecionada[i] = false;
		}
		
		//procura os pares das botas
		for (int i = 0; i < quantidade; i++) {
			if (!bota_selecionada[i]) {
				for (int j = i+1; j < quantidade; j++) {
					if ((!bota_selecionada[j]) &&
					(bota_tamanho[i] == bota_tamanho[j]) && 
						(bota_lado[i] != bota_lado[j])) {
							bota_selecionada[j] = true;
							total_pares++;
							//total_pares = total_pares+1;
							break;				
					} //if
				} //for
			} //if
		} //for
		cout<<total_pares<<endl;
		continua = cin>>quantidade;
	} //while
	return 0;
}
