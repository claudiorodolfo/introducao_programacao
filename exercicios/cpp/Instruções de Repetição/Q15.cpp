/*
------------------------------------------------
15. Crie um algoritmo/fluxograma/programa que 
leia um valor de "b" e um valor de "n", calcule 
e escreve a valor de b elevado a n (sem uso de 
função matemática). Ex: b = 5, n = 3, 
b*b*b = 125.
 */
#include <iostream>
#include <clocale>

using namespace std;

int main () {
	setlocale(LC_ALL,"Portuguese");
    int b, n, resultado = 1;
    cout<<"Informe a base e o expoente:";
    cin>>b>>n;

	for (int i = 1; i <= n; i++)
        resultado = resultado * b;

    cout<<b<<" elevado a "<<n<<" é "<<resultado;
	return 0;
}