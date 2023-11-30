/*
------------------------------------------------
5. Crie um algoritmo/fluxograma/programa que 
solicite ao usu�rio um ano e imprima se � 
bissexto ou n�o.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int ano, resto;
	cout<<"Informe o ano:";
	cin>>ano;
	resto = ano % 4;
	if (resto == 0) {
		cout<<ano<<" É um ano bissexto!";
	} else {
		cout<<ano<<" não é um ano bissexto!";
	}
	return 0;
}
