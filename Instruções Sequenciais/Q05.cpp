/*
------------------------------------------------
5. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário 2 valores, em seguida, 
troque o valor dessas variáveis e imprima os 
novos valores.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float valor1, valor2, auxiliar;
	cout<<"Informe a primeiro valor:";
	cin>>valor1;
	cout<<"Informe o segundo valor:";
	cin>>valor2;
	cout<<"Antes da troca:"<<endl;
	cout<<valor1<<"  "<<valor2<<endl;
	
	auxiliar = valor1;
	valor1 = valor2;
	valor2 = auxiliar;
	
	cout<<"Depois da troca:"<<endl;
	cout<<valor1<<"  "<<valor2<<endl;
	return 0;
}
