/*
------------------------------------------------
9. Crie um algoritmo/fluxograma/programa que 
conte e imprima o número de elementos pares em 
um array.
 */
#include <iostream>
#include <locale.h>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];
	int cont = 0;

	for (int i = 0; i < tam; i++)
		if (dado[i] % 2 == 0)
			cont++;
		
	cout<<"Há "<<cont<<" elementos pares.";
	return EXIT_SUCCESS;	
}
