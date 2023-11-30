//Problema 1021 - Notas e Moedas
//https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
/*
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 = N = 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
Obs: Utilize ponto (.) para separar a parte decimal.
*/
#include <iostream>
#include <math.h>

using namespace std;

int main() {
	float v;
	int valor;
	
	cin>> v;
	
	//70.34 internamente vira um 70.33999999999999999999
	valor = int(round(v*100));
	
	int cedulas_100 = 0;
	int cedulas_50 = 0;
	int cedulas_20 = 0;
	int cedulas_10 = 0;
	int cedulas_5 = 0;
	int cedulas_2 = 0;

	int moedas_100 = 0;
	int moedas_50 = 0;
	int moedas_25 = 0;
	int moedas_10 = 0;
	int moedas_5 = 0;
	int moedas_1 = 0;

	while (valor >= 100*100) {
		valor -= 100*100;
	//	valor = valor - 100*100;
		cedulas_100 += 1;
	//	cedulas_100 = cedulas_100 + 1;
	}
	
	while (valor >= 50*100) {
		valor -= 50*100;
		cedulas_50 += 1;
	}
		
	while (valor >= 20*100) {
		valor -= 20*100;
		cedulas_20 += 1;
	}
	
	while (valor >= 10*100) {
		valor -= 10*100;
		cedulas_10 += 1;
	}

	while (valor >= 5*100) {
		valor -= 5*100;
		cedulas_5 += 1;
	}

	while (valor >= 2*100) {
		valor -= 2*100;
		cedulas_2 += 1;
	}

	while (valor >= 100) {
		valor -= 100;
		moedas_100 += 1;
	}

	while (valor >= 50) {
		valor -= 50;
		moedas_50 += 1;
	}

	while (valor >= 25) {
		valor -= 25;
		moedas_25 += 1;
	}

	while (valor >= 10) {
		valor -= 10;
		moedas_10 += 1;
	}

	while (valor >= 5) {
		valor -= 5;
		moedas_5 += 1;
		}

    moedas_1 += valor;

	cout<<"NOTAS:"<<endl;
	cout<<cedulas_100<<" nota(s) de R$ 100.00"<<endl;
	cout<<cedulas_50<<" nota(s) de R$ 50.00"<<endl;
	cout<<cedulas_20<<" nota(s) de R$ 20.00"<<endl;
	cout<<cedulas_10<<" nota(s) de R$ 10.00"<<endl;
	cout<<cedulas_5<<" nota(s) de R$ 5.00"<<endl;
	cout<<cedulas_2<<" nota(s) de R$ 2.00"<<endl;
	cout<<"MOEDAS:"<<endl;
	cout<<moedas_100<<" moeda(s) de R$ 1.00"<<endl;
	cout<<moedas_50<<" moeda(s) de R$ 0.50"<<endl;
	cout<<moedas_25<<" moeda(s) de R$ 0.25"<<endl;
	cout<<moedas_10<<" moeda(s) de R$ 0.10"<<endl;
	cout<<moedas_5<<" moeda(s) de R$ 0.05"<<endl;
	cout<<moedas_1<<" moeda(s) de R$ 0.01"<<endl;

	return 0;
}
