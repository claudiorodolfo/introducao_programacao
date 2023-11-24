/*
------------------------------------------------
7. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário um valor de investimento. Se
o valor for maior que R$ 10.000,00, imprima 
"Investimento Alto", senão, imprima 
"Investimento Baixo".
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float valor;
	cout<<"Informe um valor de investimento:";
	cin>>valor;
	
	if (valor > 10000)
		cout<<"Investimento Alto:";		
	else
		cout<<"Investimento Baixo:";			
		
	return 0;
}
