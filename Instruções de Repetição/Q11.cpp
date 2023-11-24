/*
------------------------------------------------
11. Crie um algoritmo/fluxograma/programa que 
escreva a média de 10 números informados pelo 
usuário.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int numero, soma = 0;
	for (int i = 1; i <= 10; i++) {
		cout<<"Informe o "<<i<<"º numero:";
		cin>>numero;
		soma += numero;
	}
	cout<<"A media é: "<<soma/10;
	return 0;
}
