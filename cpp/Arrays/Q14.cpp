/*
------------------------------------------------
14. Crie um algoritmo/fluxograma/programa que 
ordene os elementos de um array em ordem
crescente.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];
	
	for (int i = 0; i < tam-1; i++)
        for (int j = 0; j < tam-1; j++)
		    if (dado[j] > dado[j+1]) {
                int aux = dado[j];
                dado[j] = dado[j+1];
                dado[j+1] = aux;
            }

	for (int i = 0; i < tam; i++)
		cout<<dado[i]<<" ";

	return EXIT_SUCCESS;	
}
