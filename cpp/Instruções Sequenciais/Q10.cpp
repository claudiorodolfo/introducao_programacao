/*
------------------------------------------------
10. Crie um algoritmo/fluxograma/programa que 
solicite ao usu�rio um n�mero decimal e, em 
seguida, calcule e imprima o valor absoluto 
desse n�mero. Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float num, resultado;
	cout<<"Informe o n�mero:";
	cin>>num;
	resultado = abs(num);
	cout<<"O m�dulo do n�mero �: ";
	cout<<resultado<<endl;
	return 0;
}

