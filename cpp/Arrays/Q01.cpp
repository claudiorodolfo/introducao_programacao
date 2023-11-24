/*
------------------------------------------------
1. Crie um algoritmo/fluxograma/programa que 
declare um array de inteiros e imprima seus 
elementos. 
 */
#include <iostream>
#include <locale.h>
//#include <vector>
//#include <array>

using namespace std;

int main () {
	setlocale(LC_ALL,"Portuguese");
	
	int dado[] = {2, 3, 9, 2, 1, 32, 0, -1};
	const int tam = sizeof dado/sizeof dado[0];
	
	//array<int, 6> dado = {2, 3, 9, 2, 1, 32};
	//vector<int> dado = {2, 3, 9, 2, 1, 32};	
  	//const int tam = dado.size();
  	//const int tam = size(dado);
	    
	for (int i = 0; i < tam; i++) {
		cout<<dado[i]<<" ";
	}
	return 0;
}
