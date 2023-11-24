/*
------------------------------------------------
2. Crie um algoritmo/fluxograma/programa que 
imprima todos os números pares entre 10 e 100.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	for (int i = 10; i <= 100; i += 2) {
		cout<<i<<" ";
	}
	return 0;
}
