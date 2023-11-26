/*
------------------------------------------------
13. Crie um programa que imprima os números de 
1 a 20 em ordem inversa.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	for (int i = 20; i >= 1; i--)
		cout<<i<<" ";

	return 0;
}
