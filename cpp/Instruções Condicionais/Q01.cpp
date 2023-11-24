/*
------------------------------------------------
1. Crie um algoritmo/fluxograma/programa que 
peça ao usuário um número de 1 a 7 e imprima o 
dia da semana correspondente.
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
			cout<<"Segunda-feira"<<endl;
			break;
		case 2:
			cout<<"Terça-feira"<<endl;
			break;
		case 3:
			cout<<"Quarta-feira"<<endl;
			break;
		case 4:
			cout<<"Quinta-feira"<<endl;
			break;
		case 5:
			cout<<"Sexta-feira"<<endl;
			break;
		case 6:
			cout<<"Sábado"<<endl;
			break;
		case 7:
			cout<<"Domingo"<<endl;
			break;			
		default:
			cout<<"Dia inválido!"<<endl;
	}
	return 0;
}
