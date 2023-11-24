/*
------------------------------------------------
3. Crie um algoritmo/fluxograma/programa que 
peça ao usuário um número e imprima os números 
de 1 até esse número.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int limite;
	cout<<"Informe o número:";
	cin>>limite;

	for (int i = 1; i <= limite; i++) {
		cout<<i<<" ";
	}
	return 0;
}
