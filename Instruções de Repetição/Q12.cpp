/*
------------------------------------------------
12. Crie um algoritmo/fluxograma/programa que 
leia uma quantidade de números, e em seguida 
leia esses números e imprima a média deles.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int quantidade, numero, soma = 0;
	cout<<"Informe qtns números serão lidos:";
	cin>>quantidade;
	for (int i = 1; i <= quantidade; i++) {
		cout<<"Informe o "<<i<<"º numero:";
		cin>>numero;
		soma += numero;
	}
	cout<<"A media é: "<<soma/quantidade;
	return 0;
}
