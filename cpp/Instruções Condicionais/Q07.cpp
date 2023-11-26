/*
------------------------------------------------
7. Crie um algoritmo/fluxograma/programa que 
solicite ao usu�rio um valor de investimento. Se
o valor for maior que R$ 10.000,00, imprima 
"Investimento Alto", sen�o, imprima 
"Investimento Baixo".
 */
#include <iostream>
#include <clocale>
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
