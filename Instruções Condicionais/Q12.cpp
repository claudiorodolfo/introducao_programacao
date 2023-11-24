/*
------------------------------------------------
12. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário um mês e um ano e imprima se
o mês indicado tem 28, 29, 30 ou 31 dias.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int ano, mes;
	cout<<"Informe o ano:";
	cin>>ano;
	cout<<"Informe o mês [1..12]:";
	cin>>mes;

	switch(mes) {
		case 1: case 3:	case 5: case 7:
		case 8: case 10: case 12:
			cout<<"O mês tem 31 dias.";
			break;
		case 2: case 4:	case 6:	case 9: case 11:
			if (mes == 2) {
				int resto = ano % 4;
				if (resto == 0) {
					cout<<"O mês tem 29 dias.";
				} else {
					cout<<"O mês tem 28 dias.";
				}
			} else {
				cout<<"O mês tem 30 dias.";
			}
			break;
		default:
			cout<<"Mês inválido!"<<endl;
	}
	return 0;
}
