/*
------------------------------------------------
10. Crie um algoritmo/fluxograma/programa que 
imprima a soma dos quadrados dos números de 
1 a 10.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int soma = 0;
	for (int i = 1; i <= 10; i++) {
		soma = soma + i*i;
		//soma += (i*i);
	}
	cout<<"A soma é: "<<soma;
	return 0;
}
