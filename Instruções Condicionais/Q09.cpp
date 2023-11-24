/*
-------------------------------------------------
9. Crie um algoritmo/fluxograma/programa que leia 
um número inteiro e escreva se ele é par ou 
ímpar.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int numero;
	cout<<"Informe um numero:";
	cin>>numero;
	
	if (numero % 2 == 0)
		cout<<"Par"<<endl;
	else
		cout<<"Impar"<<endl;
		
	return 0;
}
