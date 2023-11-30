/*
------------------------------------------------
17. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário o valor do raio de uma 
esfera e calcule e imprima o volume dessa 
esfera. 
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double volume, raio;
	cout<<"Informe o raio (m):";
	cin>>raio;  
    volume = 4/3 * M_PI * pow(raio, 3);
    cout<<"Volume:"<<volume<<" m³"<<endl;
	return 0;
}