/*
------------------------------------------------
9. Crie um algoritmo/fluxograma/programa que 
peça ao usuário para inserir dois números 
inteiros e, em seguida, imprima o resultado 
arredondado da divisão do primeiro pelo segundo.
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int num1, num2;
	float resultado;
	cout<<"Informe a primeiro número:";
	cin>>num1;
	cout<<"Informe o segundo número:";
	cin>>num2;	
	resultado = round((float)num1 /(float)num2);
	cout<<"A divisão arredondada é: ";
	cout<<resultado<<endl;
	return 0;
}

