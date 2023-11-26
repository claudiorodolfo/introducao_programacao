/*
------------------------------------------------
12. Crie um algoritmo/fluxograma/programa que 
declare uma vari�vel do tipo ponto flutuante e 
atribua a ela um valor. Em seguida, calcule e 
imprima a raiz quadrada desse valor. Usar a 
biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float valor;
	double resultado;
	cout<<"Informe um valor:";
	cin>>valor;
	//resultado = pow(valor, 0.5);
	//resultado = pow(valor, 1/2);	
	resultado = sqrt(valor);
	cout<<" raiz quadrada de "<<valor<<" é ";
	cout<<resultado<<endl;
	return 0;
}


