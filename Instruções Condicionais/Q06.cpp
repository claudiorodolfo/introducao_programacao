/*
------------------------------------------------
6. Crie um algoritmo/fluxograma/programa que 
leia um número e se este número for maior do que
20, imprima a metade dele.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float numero;
	cout<<"Informe um número:";
	cin>>numero;
	
	if (numero < 20)
		cout<<numero/2;
		
	return 0;
}
