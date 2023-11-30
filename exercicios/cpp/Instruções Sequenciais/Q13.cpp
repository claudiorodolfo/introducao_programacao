/*
------------------------------------------------
14. Crie um algoritmo/fluxograma/programa que 
peça ao usuário para inserir um número decimal 
e, em seguida, calcule e imprima a parte 
fracionária desse número.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double valor = 125.0;
    double resultado = pow(valor, (double)1/3);	

	cout<<" raiz cúbica de "<<valor<<" é ";
	cout<<resultado<<endl;
	return 0;
}