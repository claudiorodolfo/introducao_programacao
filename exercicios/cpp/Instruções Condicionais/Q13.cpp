/*
------------------------------------------------
13. Crie um algoritmo/fluxograma/programa que 
peça ao usuário o valor de um produto e, se esse
valor for maior que R$ 100, aplique um desconto 
de 5%.
 */
#include <iostream>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float valor;
	cout<<"Informe um valor:";
	cin>>valor;
    if (valor > 100.0) {
        valor = valor * 0.95;
    }
    cout<<"Valor Final:"<<valor;
	return 0;
}