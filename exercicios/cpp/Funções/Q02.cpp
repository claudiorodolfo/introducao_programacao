/*
------------------------------------------------
2. Crie uma função para calcular e retornar a 
área de um círculo, que tenha o raio informado 
pelo usuário.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>
#include <cmath>

using namespace std;

float calculaArea(float r) {
	return M_PI * r * r;
}

int main() {
	setlocale(LC_ALL,"Portuguese");
	float raio, area;
	cout<<"Informe o raio (m):";
	cin>>raio;
	area = calculaArea(raio);
	cout<<"A área é:"<<area<<" m².";
	return EXIT_SUCCESS;	
}