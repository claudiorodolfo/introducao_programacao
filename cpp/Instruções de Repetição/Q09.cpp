/*
------------------------------------------------
9. Crie um algoritmo/fluxograma/programa que 
calcule a soma dos n�meros de 1 a 100.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int soma = 0;
	for (int i = 1; i <= 100; i++) {
		soma = soma + i;
		//soma += i;
	}
	cout<<"A soma é: "<<soma;
	return 0;
}
