/*
------------------------------------------------
7. Crie um algoritmo/fluxograma/programa que 
declare uma variável do tipo ponto flutuante e 
atribua a ela um valor informado pelo usuário. 
Em seguida, arredonde esse valor para duas casas
decimais e imprima o resultado. Usar a 
biblioteca iomanip.
 */
#include <iostream>
#include <iomanip>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float valor;
	cout<<"Informe um valor real:";
	cin>>valor;
	cout<<fixed<<setprecision(2)<<valor;
	return 0;
}
