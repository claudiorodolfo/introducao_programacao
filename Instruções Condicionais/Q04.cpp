/*
------------------------------------------------
4. Crie um algoritmo/fluxograma/programa que 
solicite ao usu�rio o c�digo de um produto e 
imprima a categoria dele: 1 a 10 (Alimenta��o), 
11 a 20 (Limpeza), 21 a 30 (Eletr�nicos).
 */
#include <iostream>
#include <locale.h>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	int codigo;
	cout<<"Informe o c�digo do produto:";
	cin>>codigo;
	//pode-se fazer com switch..case, if..else
	if (codigo >= 1 && codigo <= 10) {
		cout<<"Alimenta��o"<<endl;
	}
	if (codigo >=11 && codigo <= 20) {
		cout<<"Limpeza"<<endl;		
	}
	if (codigo >=21 && codigo <= 30) {
		cout<<"Eletr�nicos"<<endl;		
	}		
	return 0;
}
