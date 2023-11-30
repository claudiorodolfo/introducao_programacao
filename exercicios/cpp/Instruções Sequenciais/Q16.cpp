/*
------------------------------------------------
16. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário o raio da base e a altura 
de uma caixa d'água cilíndrica, calcule, e 
imprima na tela o seu volume em litros. 
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double area, raio, altura;
	cout<<"Informe o raio (m):";
	cin>>raio;
	cout<<"Informe a altura (m):";
	cin>>altura;    
    area = M_PI * pow(raio, 2) * altura;
    cout<<"Volume:"<<area<<" m³"<<endl;
	return 0;
}