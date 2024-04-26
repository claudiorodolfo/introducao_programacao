#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;

int main() { 
	setlocale(LC_ALL, "Portuguese");
	string pessoa, computador;
	
	int sorteio = rand() % 3;
	switch (sorteio) {
		case 0:
			computador = "pedra";
			break;
		case 1:			
			computador = "papel";
			break;
		case 2:			
			computador = "tesoura";
			break;						
	}
	
	cout<<"Escolha uma op��o ";
	cout<<"[pedra, papel, tesoura]:";
	cin>>pessoa;
	
	if (pessoa == computador) {
		cout<<"Empate";
	} else {
		if (pessoa == "pedra") {
			if (computador == "papel")
				cout<<"Computador ganhou!";
			else	//Tesoura
				cout<<"Voc� ganhou!";				
		}
		
		if (pessoa == "papel") {
			if (computador == "tesoura")
				cout<<"Computador ganhou!";
			else	//pedra
				cout<<"Voc� ganhou!";				
		}
	
		if (pessoa == "tesoura") {
			if (computador == "pedra")
				cout<<"Computador ganhou!";
			else	//papel
				cout<<"Voc� ganhou!";					
		}
	}
	return 0;	
}
