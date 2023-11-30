/*
------------------------------------------------
3. Crie um algoritmo/fluxograma/programa que 
pe�a ao usu�rio um n�mero e imprima os n�meros 
de 1 at� esse n�mero.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int limite;
	cout<<"Informe o número:";
	cin>>limite;

	for (int i = 1; i <= limite; i++) {
		cout<<i<<" ";
	}
	return 0;
}
