/*
------------------------------------------------
12. Crie um algoritmo/fluxograma/programa que 
leia uma quantidade de n�meros, e em seguida 
leia esses n�meros e imprima a m�dia deles.
 */
#include <iostream>
#include <clocale>
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
