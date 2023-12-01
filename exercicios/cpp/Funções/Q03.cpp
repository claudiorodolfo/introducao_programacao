/*
------------------------------------------------
3. Crie uma função para calcular o preço final 
após aplicar um desconto em um valor inserido 
pelo usuário.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;

float calcula(float p, float d) {
	return (p * (1-d/100));
}

int main() {
	setlocale(LC_ALL,"Portuguese");
	float preco, desconto;
	cout<<"Informe preço e desconto [0%..100%]:";
	cin>>preco>>desconto;
	float final = calcula(preco, desconto);
	cout<<"Preço com desconto: R$ "<<final;
	return EXIT_SUCCESS;	
}