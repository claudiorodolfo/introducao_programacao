/*
------------------------------------------------
7. Crie um algoritmo/fluxograma/programa que 
imprima os números de 1 a 50, pulando os 
múltiplos de 4 e 5.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");

	for (int i = 1; i <= 50; i++)
		if (i % 4 != 0 && i % 5 != 0)
			cout<<i<<endl;

	return 0;
}
