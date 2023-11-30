/*
------------------------------------------------
2. Crie um algoritmo/fluxograma/programa que 
peca ao usuario um numero de 1 a 12 e imprima o 
mes correspondente.
 */
#include <iostream>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int mes;
	cout<<"Informe um número referente a um ";
	cout<<"mês [1..12]:";
	cin>>mes;
	switch(mes) {
		case 1:
			cout<<"Janeiro"<<endl;
			break;
		case 2:
			cout<<"Fevereiro"<<endl;
			break;
		case 3:
			cout<<"Março"<<endl;
			break;
		case 4:
			cout<<"Abril"<<endl;
			break;
		case 5:
			cout<<"Maio"<<endl;
			break;
		case 6:
			cout<<"Junho"<<endl;
			break;
		case 7:
			cout<<"Julho"<<endl;
			break;
		case 8:
			cout<<"Agosto"<<endl;
			break;
		case 9:
			cout<<"Setembro"<<endl;
			break;
		case 10:
			cout<<"Outubro"<<endl;
			break;
		case 11:
			cout<<"Novembro"<<endl;
			break;
		case 12:
			cout<<"Dezembro"<<endl;
			break;
		default:
			cout<<"Mês inválido!"<<endl;
	}
	return 0;
}
