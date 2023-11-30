/*
------------------------------------------------
20. Crie um algoritmo/fluxograma/programa que 
leia a altura, a base maior e a base menor 
referentes a um trapézio, calcule e mostre na 
tela a sua área.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double area, b_maior, b_menor, alt;
	cout<<"Informe a base maior:";
	cin>>b_maior;
	cout<<"Informe a base menor:";
	cin>>b_menor;    
	cout<<"Informe a altura:";
	cin>>alt;  
    area = ((b_maior + b_menor)*alt)/2;    
    cout<<"A área do trapézio é:"<<area<<endl;
	return 0;
}