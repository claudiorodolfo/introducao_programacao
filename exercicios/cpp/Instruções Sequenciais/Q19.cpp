/*
------------------------------------------------
19. Crie um algoritmo/fluxograma/programa que 
leia os catetos de um triângulo retângulo, 
calcule e escreva a hipotenusa correspondente. 
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double cat1, cat2, hip;
	cout<<"Informe o primeiro cateto:";
	cin>>cat1;
	cout<<"Informe o segundo cateto:";
	cin>>cat2;  
    hip = sqrt(cat1*cat1 + cat2*cat2);       
    cout<<"A hipotenusa é:"<<hip<<endl;
	return 0;
}