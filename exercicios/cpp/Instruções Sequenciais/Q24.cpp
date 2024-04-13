#include <iostream>
#include <clocale>
#include <string>

using namespace std;

int main() {
	setlocale(LC_ALL,"Portuguese");	
	string nome = "Cláudio Rodolfo Machado de Oliveira";
	string antigoSobrenome = "Machado";
	string novoSobrenome = "Silva";
	cout<<"Antes: "<<nome<<endl;
	size_t posicaoSobrenome = nome.find(antigoSobrenome);
	nome.replace(posicaoSobrenome, antigoSobrenome.size(), novoSobrenome);
	cout<<"Depois:"<<nome<<endl;
    return 0;
}
