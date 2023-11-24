/*
------------------------------------------------
10. Crie um algoritmo/fluxograma/programa que 
leia um número e imprima se ele é positivo, 
negativo ou neutro.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int numero;
	cout<<"Informe um numero:";
	cin>>numero;
	
	if (numero < 0)
		cout<<"Negativo"<<endl;
	if (numero > 0)
		cout<<"Positivo"<<endl;	
	else
		cout<<"Neutro"<<endl;
		
	return 0;
}
