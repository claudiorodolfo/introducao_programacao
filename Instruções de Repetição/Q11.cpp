/*
------------------------------------------------
11. Crie um algoritmo/fluxograma/programa que 
escreva a m�dia de 10 n�meros informados pelo 
usu�rio.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int numero, soma = 0;
	for (int i = 1; i <= 10; i++) {
		cout<<"Informe o "<<i<<"� numero:";
		cin>>numero;
		soma += numero;
	}
	cout<<"A media �: "<<soma/10;
	return 0;
}
