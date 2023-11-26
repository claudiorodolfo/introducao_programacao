/*
------------------------------------------------
14. Crie um algoritmo/fluxograma/programa que 
imprima a raiz quadrada de todos os números de
100 até 1.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;

int main () {
	setlocale(LC_ALL,"Portuguese");
	for (int i = 100; i >= 1; i--)
		cout<<i<<" "<<sqrt(i)<<endl;

	return 0;
}