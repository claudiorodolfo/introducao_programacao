/*
------------------------------------------------
15. Crie um algoritmo/fluxograma/programa que 
preencha um array com números aleatórios e, em
seguida, ordene esses números de forma 
decrescente.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
    const int tam = 8;
    int dado[tam];

    //numeros aleatório entre 21 e 30
    for (int i = 0; i < tam; i++)
        dado[i] = rand() % 10 + 21;

	for (int i = 0; i < tam-1; i++)
        for (int j = 0; j < tam-1; j++)
		    if (dado[j] < dado[j+1]) {
                int aux = dado[j];
                dado[j] = dado[j+1];
                dado[j+1] = aux;
            }

	for (int i = 0; i < tam; i++)
		cout<<dado[i]<<" ";

	return EXIT_SUCCESS;	
}
