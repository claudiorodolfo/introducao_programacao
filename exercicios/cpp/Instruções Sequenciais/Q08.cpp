/*
------------------------------------------------
8. Crie um algoritmo/fluxograma/programa que 
leia um �ngulo em graus, calcule e imprima o 
seno e o cosseno dele. Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float angulo, seno, cosseno;
	cout<<"Informe um ângulo (em º):";
	cin>>angulo;
	seno = sin(angulo * M_PI/180);
	cosseno = cos(angulo * M_PI/180);	
	cout<<"   O seno de "<<angulo<<" º ";
	cout<<seno<<endl;
	cout<<"O cosseno de "<<angulo<<" º ";
	cout<<cosseno<<endl;
	return 0;
}
