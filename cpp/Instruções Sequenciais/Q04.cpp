/*
------------------------------------------------
4. Crie um algoritmo/fluxograma/programa que l� 
o nome de um aluno, as notas de suas tr�s provas
e calcule e exiba na tela a m�dia harm�nica das 
provas.
 */
#include <iostream>
#include <clocale>
using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	string nome;
	float nota1, nota2, nota3, media;
	cout<<"Informe o nome do aluno:";
	cin>>nome;
	cout<<"Informe a nota 1:";
	cin>>nota1;
	cout<<"Informe a nota 2:";
	cin>>nota2;
	cout<<"Informe a nota 3:";
	cin>>nota3;	
	media = 3 / (1/nota1 + 1/nota2 + 1/nota3);
	cout<<"A media harmônica de "<<nome<<" é:";
	cout<<media<<endl;
	return 0;
}
