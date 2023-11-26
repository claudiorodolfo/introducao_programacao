/*
------------------------------------------------
14. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário o peso de um produto. Se o
peso for maior que 10 kg, calcule o frete com 
20% de acréscimo; caso contrário, aplique frete
normal.
 */
#include <iostream>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float peso, frete = 1.0;
	cout<<"Informe um peso (kg):";
	cin>>peso;
    if (peso > 10.0) {
        frete = frete * 1.2;
    }
    cout<<"Valor Final:"<<peso + frete;
	return 0;
}