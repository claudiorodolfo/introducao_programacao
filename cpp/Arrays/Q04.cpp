/*
------------------------------------------------
4. Crie um algoritmo/fluxograma/programa que 
encontre o maior e o menor n�mero em um array e 
imprima-os na tela.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 2, 34, -7};
	const int tam = sizeof dado/sizeof dado[0];
	
	int menor = 1000000;
	int maior = -1000000;
	for (int i = 0; i < tam; i++) {
		if (dado[i] < menor)
			menor = dado[i];
		
		if (dado[i] > maior)
			maior = dado[i];		
	}
	cout<<"Menor:"<<menor<<endl;
	cout<<"Maior:"<<maior<<endl;	
	return EXIT_SUCCESS;
}
