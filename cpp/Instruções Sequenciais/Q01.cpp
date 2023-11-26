/*
------------------------------------------------
1. Crie um algoritmo/fluxograma/programa que 
leia dois valores num�ricos, e calcule e exiba 
na tela a m�dia aritm�tica deles. 
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float a, b, media;
	cout<<"Informe o primeiro valor:";
	cin>>a;
	cout<<"Informe o segundo valor:";
	cin>>b;
	media = (a + b) / 2;
	cout<<"A media é:"<<media;
	return 0;
}
