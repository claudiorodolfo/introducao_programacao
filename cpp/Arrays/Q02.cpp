/*
------------------------------------------------
2. Crie um algoritmo/fluxograma/programa que 
preencha um array com os quadrados dos n�meros 
de 1 a N, onde N � um valor informado pelo 
usu�rio. 
 */
#include <iostream>
#include <cmath>
#include <locale.h>

using namespace std;

int main () {
	setlocale(LC_ALL,"Portuguese");
	int n;
	
	cout<<"Informe um valor:";
	cin>>n;
	int dado[n];
		    
	for (int i = 0; i < n; i++) {
		dado[i] = pow(i+1, 2);
	}
	
	//impress�o pra ver se t� certo
	for (int i = 0; i < n; i++) {
		cout<<dado[i] <<" ";
	}
	return 0;
}
