/*
------------------------------------------------
5. Crie um algoritmo/fluxograma/programa que 
imprima os n�meros de 1 a 100, mas substitua os 
m�ltiplos de 3 por "Fizz" e os m�ltiplos de 5 
por "Buzz".
 */
#include <iostream>
#include <clocale>
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
