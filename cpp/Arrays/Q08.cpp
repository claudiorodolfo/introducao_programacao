/*
------------------------------------------------
8. Crie um algoritmo/fluxograma/programa que 
multiplique cada elemento de um array por um
valor específico. Mostre o antes e o depois.
 */
#include <iostream>
#include <locale.h>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];
	int valor = 10;
	//antes
	for (int i = 0; i < tam; i++)
		cout<<dado[i]<<" ";
	cout<<endl;
			
	for (int i = 0; i < tam; i++)
		dado[i] *= valor;

	//depois
	for (int i = 0; i < tam; i++)
		cout<<dado[i]<<" ";
	cout<<endl;
	
	return EXIT_SUCCESS;	
}
