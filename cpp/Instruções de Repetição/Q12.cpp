/*
------------------------------------------------
12. Crie um algoritmo/fluxograma/programa que 
leia uma quantidade de n�meros, e em seguida 
leia esses n�meros e imprima a m�dia deles.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int quantidade, numero, soma = 0;
	cout<<"Informe qtns n�meros ser�o lidos:";
	cin>>quantidade;
	for (int i = 1; i <= quantidade; i++) {
		cout<<"Informe o "<<i<<"� numero:";
		cin>>numero;
		soma += numero;
	}
	cout<<"A media �: "<<soma/quantidade;
	return 0;
}
