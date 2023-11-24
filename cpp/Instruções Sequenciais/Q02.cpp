/*
------------------------------------------------
2. Crie um algoritmo/fluxograma/programa que 
leia 2 valores e escreva na tela a média 
ponderada entre eles. O primeiro valor tem peso 
40%, e o segundo valor tem peso 60%.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float a, b, media;
	cout<<"Informe o primeiro valor:";
	cin>>a;
	cout<<"Informe o segundo valor:";
	cin>>b;
	media = a*0.4 + b*0.6;
	cout<<"A média ponderada é:"<<media;
	return 0;
}
