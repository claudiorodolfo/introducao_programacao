/*
------------------------------------------------
13. Crie um algoritmo/fluxograma/programa que 
copie os elementos de um array para outro.
Imprima-os para mostrar que estão iguais.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];

    int outro[tam];
	
	for (int i = 0; i < tam; i++)
		outro[i] = dado[i];

    cout<<"DADO"<<endl;
	for (int i = 0; i < tam; i++)
		cout<<dado[i]<<" ";
    cout<<endl;

    cout<<"OUTRO"<<endl;
	for (int i = 0; i < tam; i++)
		cout<<outro[i]<<" ";

	return EXIT_SUCCESS;	
}
