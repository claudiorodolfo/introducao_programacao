/*
------------------------------------------------
4. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário o código de um produto e 
imprima a categoria dele: 1 a 10 (Alimentação), 
11 a 20 (Limpeza), 21 a 30 (Eletrônicos).
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int codigo;
	cout<<"Informe o código do produto:";
	cin>>codigo;
	//pode-se fazer com switch..case, if..else
	if (codigo >= 1 && codigo <= 10) {
		cout<<"Alimentação"<<endl;
	}
	if (codigo >=11 && codigo <= 20) {
		cout<<"Limpeza"<<endl;		
	}
	if (codigo >=21 && codigo <= 30) {
		cout<<"Eletrônicos"<<endl;		
	}		
	return 0;
}
