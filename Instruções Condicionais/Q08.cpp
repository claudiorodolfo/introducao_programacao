/*
------------------------------------------------
8. Crie um algoritmo/fluxograma/programa que 
leia um n�mero e imprima o seu valor absoluto, 
independente dele ser positivo ou negativo, sem 
uso de biblioteca matem�tica.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float numero;
	cout<<"Informe um numero:";
	cin>>numero;
	
	if (numero < 0) {
		numero *= -1; 
		//numero = numero * (-1);
	}
			
	cout<<"O m�dulo do numero informado �: ";
	cout<<numero;	
		
	return 0;
}
