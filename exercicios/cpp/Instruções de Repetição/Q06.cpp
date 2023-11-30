/*
------------------------------------------------
6. Crie um algoritmo/fluxograma/programa que 
imprima os números de 1 a 50, que sejam 
múltiplos de 3 e 7 ao mesmo tempo.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");

	for (int i = 1; i <= 50; i++)
		if (i % 3 == 0 && i % 7 == 0)
			cout<<i<<endl;

	return 0;
}
