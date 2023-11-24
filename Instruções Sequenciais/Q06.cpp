/*
------------------------------------------------
6. Crie um algoritmo/fluxograma/programa que 
peça ao usuário para inserir dois números 
inteiros e, em seguida, imprima o resultado da 
divisão do primeiro pelo segundo, considerando 
somente a parte inteira.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float num1, num2, divisao;
	cout<<"Informe a primeiro número:";
	cin>>num1;
	cout<<"Informe o segundo número:";
	cin>>num2;
	divisao = (int) (num1 / num2);
	cout<<"Resultado:"<<divisao;
	return 0;
}
