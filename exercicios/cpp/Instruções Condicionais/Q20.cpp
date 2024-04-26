#include <iostream>
#include <clocale>

using namespace std;

int main() { 
	setlocale(LC_ALL, "Portuguese");
	float valor1, valor2, maior;
	cout<<"Informe o primeiro valor:";
	cin>>valor1;
	cout<<"Informe o segundo valor:";
	cin>>valor2;
	maior = (valor1 > valor2) ? valor1 : valor2;
	
	cout<<"O maior valor é: "<<maior;
	return 0;
}
