/*
------------------------------------------------
3. Crie um algoritmo/fluxograma/programa que 
leia 3 valores e escreva na tela a m�dia 
ponderada entre eles. O primeiro valor tem peso 
4, o segundo valor tem peso 7 e o terceiro valor
tem peso 3. 
 */
#include <iostream>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float a, b, c, media;
	cout<<"Informe o primeiro valor:";
	cin>>a;
	cout<<"Informe o segundo valor:";
	cin>>b;
	cout<<"Informe o terceiro valor:";
	cin>>c;	
	media = (a*4 + b*7 + c*3) / 14;
	cout<<"A média ponderada é:"<<media;
	return 0;
}
