/*
------------------------------------------------
10. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário um número decimal e, em 
seguida, calcule e imprima o valor absoluto 
desse número. Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float num, resultado;
	cout<<"Informe o número:";
	cin>>num;
	resultado = abs(num);
	cout<<"O módulo do número é: ";
	cout<<resultado<<endl;
	return 0;
}

