/*
------------------------------------------------
3. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário um número de 1 a 7 
representando um dia da semana. Imprima se é um 
dia útil ou final de semana.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int dia;
	cout<<"Informe o dia da semana [1..7]:";
	cin>>dia;
	switch(dia) {
		case 1:		
		case 2:
		case 3:
		case 4:
		case 5:
			cout<<"Dia útil"<<endl;
			break;
		case 6:
		case 7:
			cout<<"Fim de Semana"<<endl;
			break;			
		default:
			cout<<"Dia inválido!"<<endl;																																
	}
	return 0;
}

