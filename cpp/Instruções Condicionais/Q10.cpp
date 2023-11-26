/*
------------------------------------------------
10. Crie um algoritmo/fluxograma/programa que 
leia um n�mero e imprima se ele � positivo, 
negativo ou neutro.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int numero;
	cout<<"Informe um número:";
	cin>>numero;
	
	if (numero < 0)
		cout<<"Negativo"<<endl;
	if (numero > 0)
		cout<<"Positivo"<<endl;	
	else
		cout<<"Neutro"<<endl;
		
	return 0;
}
