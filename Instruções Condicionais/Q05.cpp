/*
-------------------------------------------------
5. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário um ano e imprima se é 
bissexto ou não.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int ano, resto;
	cout<<"Informe o ano:";
	cin>>ano;
	resto = ano % 4;
	if (resto == 0) {
		cout<<ano<<" é um ano bissexto!"<<endl;
	} else {
		cout<<ano<<" não um ano bissexto!"<<endl;	
	}
	return 0;
}
