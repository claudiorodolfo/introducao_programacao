/*
------------------------------------------------
5. Crie um algoritmo/fluxograma/programa que 
encontre o segundo maior elemento em um array.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;
int main() {
	setlocale(LC_ALL,"Portuguese");
	int dado[] = {-3, 0, 8, -1, 13, 7, 34, -6};
	const int tam = sizeof dado/sizeof dado[0];	

	int maior = -1000001;
	int segMaior = -1000000;
	if (tam < 2) {
		cout<<"Quantidade insuficiente!";
	}	else {
		for (int i = 0; i < tam; i++) {
			if (dado[i] > maior) {
				segMaior = maior;
				maior = dado[i];
			} else {
				if (dado[i] > segMaior && 
						dado[i] != maior) {
					segMaior = dado[i];
				} //if
			} //if
		} //for
	} //if
	
	cout<<"Segundo Maior:"<<segMaior<<endl;
	return EXIT_SUCCESS;	
}
