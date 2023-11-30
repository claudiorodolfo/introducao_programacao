/*
------------------------------------------------
4. Crie um algoritmo/fluxograma/programa que 
imprima a tabuada de multiplica��o de um n�mero 
fornecido pelo usu�rio.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int numero;
	cout<<"Informe o número:";
	cin>>numero;

	for (int i = 1; i <= 10; i++) {
		cout<<numero<<" x "<<i<<" = "<<numero*i;
		cout<<endl;
	}
	return 0;
}
