/*
------------------------------------------------
11. Crie um algoritmo/fluxograma/programa que 
solicite três números ao usuário e imprima se 
eles estão em ordem crescente.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int num1, num2, num3;
	cout<<"Informe o primeiro numero:";
	cin>>num1;
	cout<<"Informe o segundo numero:";
	cin>>num2;
	cout<<"Informe o terceiro numero:";
	cin>>num3;

	if (num1 <= num2 && num2 <= num3)
		cout<<"Estão em ordem crescente"; 
	else if (num1 >= num2 && num2 >= num3)
		cout<<"Estão em ordem decrescente";
	else
		cout<<"Estão fora de ordem";

	return 0;
}
