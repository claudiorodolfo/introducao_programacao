#include <iostream>
#include <clocale>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() { 
	setlocale(LC_ALL, "Portuguese");
	string pessoa, computador;
	
	srand(time(NULL));
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
	
	cout<<"Escolha uma opção ";
	cout<<"[pedra, papel, tesoura]:";
	cin>>pessoa;
	
	if (pessoa == computador) {
		cout<<"Empate"<<endl;
	} else {
		if (pessoa == "pedra") {
			if (computador == "papel")
				cout<<"Computador ganhou!"<<endl;
			else	//Tesoura
				cout<<"Você ganhou!"<<endl;	
		}
		
		if (pessoa == "papel") {
			if (computador == "tesoura")
				cout<<"Computador ganhou!"<<endl;
			else	//pedra
				cout<<"Você ganhou!"<<endl;
		}
	
		if (pessoa == "tesoura") {
			if (computador == "pedra")
				cout<<"Computador ganhou!"<<endl;
			else	//papel
				cout<<"Você ganhou!"<<endl;					
		}
	}
	cout<<"Pessoa:    "<<pessoa<<endl;
	cout<<"Computador:"<<computador<<endl;
	return 0;	
}
