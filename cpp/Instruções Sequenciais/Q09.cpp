/*
------------------------------------------------
9. Crie um algoritmo/fluxograma/programa que 
pe�a ao usu�rio para inserir dois n�meros 
inteiros e, em seguida, imprima o resultado 
arredondado da divis�o do primeiro pelo segundo.
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>
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

