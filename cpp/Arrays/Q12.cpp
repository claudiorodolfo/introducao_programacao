/*
------------------------------------------------
12. Crie um algoritmo/fluxograma/programa que 
verifique e informe se um determinado valor est�
presente em um array.
 */
#include <iostream>
#include <locale.h>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];
	bool estaPresente = false;
	int valor = 34;
	//int valor = 10;
	
	for (int i = 0; i < tam; i++)
		if (dado[i] == valor) {
			estaPresente = true;
			break;
		}	
			
	if (estaPresente)
		cout<<"Est� presente!";
	else
		cout<<"N�o est� presente!";
			
	return EXIT_SUCCESS;	
}
