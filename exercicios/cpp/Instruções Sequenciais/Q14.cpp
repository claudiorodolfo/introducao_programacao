/*
------------------------------------------------
13. Crie um algoritmo/fluxograma/programa que 
declare uma variável do tipo ponto flutuante e 
atribua a ela um valor. Em seguida, calcule e 
imprima a raiz cúbica desse valor.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double valor;
	int parteInteira;
	cout<<"Informe um valor:";
	cin>>valor;
    parteInteira = valor;
    cout<<"Parte fracionada:";
    cout<<abs(valor-parteInteira);
	return 0;
}