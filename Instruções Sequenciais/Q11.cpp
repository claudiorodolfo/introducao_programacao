/*
-------------------------------------------------
11. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário dois números inteiros e, em 
seguida, imprima o resultado da potenciação do 
primeiro pelo segundo. Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int num1, num2;
	double resultado;
	cout<<"Informe a base:";
	cin>>num1;
	cout<<"Informe o expoente:";
	cin>>num2;	
	resultado = pow(num1, num2);
	cout<<num1<<" elevado a "<<num2<<" é ";
	cout<<resultado<<endl;
	return 0;
}

