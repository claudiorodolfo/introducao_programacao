/*
------------------------------------------------
8. 2. Crie um algoritmo/fluxograma/programa que 
leia 5 n�meros e imprima o quadrado de cada um 
deles.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float numero;
	for (int i = 1; i <= 5; i++) {
		cout<<"Informe o "<<i<<"º numero:";
		cin>>numero;
		cout<<numero<<"² é "<<numero*numero;
		cout<<endl;
	}
	return 0;
}
