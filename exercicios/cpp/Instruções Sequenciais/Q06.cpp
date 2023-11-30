/*
------------------------------------------------
6. Crie um algoritmo/fluxograma/programa que 
pe�a ao usu�rio para inserir dois n�meros 
inteiros e, em seguida, imprima o resultado da 
divis�o do primeiro pelo segundo, considerando 
somente a parte inteira.
 */
#include <iostream>
#include <clocale>
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
