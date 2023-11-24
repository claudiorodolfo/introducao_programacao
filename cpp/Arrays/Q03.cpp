/*
------------------------------------------------
3. Crie um algoritmo/fluxograma/programa que 
preencha um array com os números em ordem 
inversa.
 */
#include <iostream>
#include <locale.h>
#include <cstdlib>

using namespace std;

int main() {
	setlocale(LC_ALL,"Portuguese");
		
	const int tam = 10;
	int dado[tam];
	for (int i = 0; i < tam; i++) 
		dado[i] = (tam-1)-i;	
	
	for (int i = 0; i < tam; i++) 
		cout<<dado[i]<<" ";
		
	return EXIT_SUCCESS;
}
