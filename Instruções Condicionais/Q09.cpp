/*
-------------------------------------------------
9. Crie um algoritmo/fluxograma/programa que leia 
um n�mero inteiro e escreva se ele � par ou 
�mpar.
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
