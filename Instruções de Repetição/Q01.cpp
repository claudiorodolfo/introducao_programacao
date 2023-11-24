/*
------------------------------------------------
1. Crie um algoritmo/fluxograma/programa que 
imprima os números de 1 a 10.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	for (int i = 1; i <= 10; i++) {
		cout<<i<<" ";
	}
	return 0;
}
