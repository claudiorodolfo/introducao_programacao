/*
------------------------------------------------
11. Crie um algoritmo/fluxograma/programa que 
solicite tr�s n�meros ao usu�rio e imprima se 
eles est�o em ordem crescente.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int num1, num2, num3;
	cout<<"Informe o primeiro número:";
	cin>>num1;
	cout<<"Informe o segundo número:";
	cin>>num2;
	cout<<"Informe o terceiro número:";
	cin>>num3;

	if (num1 <= num2 && num2 <= num3)
		cout<<"Est�o em ordem crescente"; 
	else if (num1 >= num2 && num2 >= num3)
		cout<<"Est�o em ordem decrescente";
	else
		cout<<"Est�o fora de ordem";

	return 0;
}
