/*
------------------------------------------------
1. Crie um algoritmo/fluxograma/programa que 
declare um array de inteiros e imprima seus 
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {2, 3, 9, 2, 1, 32, 0, -1};
	const int tam = sizeof dado/sizeof dado[0];
	
	for (int i = 0; i < tam; i++) {
		cout<<dado[i]<<" ";
	}
	return 0;
}
