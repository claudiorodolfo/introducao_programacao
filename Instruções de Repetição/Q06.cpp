/*
------------------------------------------------
6. Crie um algoritmo/fluxograma/programa que 
imprima os números de 1 a 50, excluindo os 
múltiplos de 3 e 7.
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");

	for (int i = 1; i <= 100; i++) {
		if (i % 3 == 0 || i % 5 == 0) {
			if (i % 3 == 0)
				cout<<"Fizz";
			if (i % 5 == 0)
				cout<<"Buzz";	
			cout<<endl;
		} else {
			cout<<i<<endl;
		}					
	}
	return 0;
}
