
/*
------------------------------------------------
6. Crie um algoritmo/fluxograma/programa que 
calcule e mostre a soma de todos os elementos 
em um array.
 */
#include <iostream>
#include <locale.h>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 2, 34, -7};
	const int tam = sizeof dado/sizeof dado[0];
	
	int soma = 0;
	for (int i = 0; i < tam; i++) {
		soma += dado[i];
		//soma = soma + dado[i];		
	}
	cout<<"Soma:"<<soma<<endl;
	return EXIT_SUCCESS;	
}
