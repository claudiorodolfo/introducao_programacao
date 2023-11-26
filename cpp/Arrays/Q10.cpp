/*
------------------------------------------------
10. Crie um algoritmo/fluxograma/programa que 
substitua todos os elementos negativos em um 
array por zero.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];

	for (int i = 0; i < tam; i++)
		if (dado[i] < 0)
			dado[i] = 0;

	for (int i = 0; i < tam; i++)
		cout<<dado[i]<<" ";
	cout<<endl;
			
	return EXIT_SUCCESS;	
}
