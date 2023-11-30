/*
------------------------------------------------
15. Crie um algoritmo/fluxograma/programa que 
solicite ao usuário o raio e calcule e imprima 
o perímetro e a área do círculo correspondente. 
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double raio;
	int perimetro, area;
	cout<<"Informe o raio:";
	cin>>raio;
    perimetro = 2 * M_PI * raio;
    area = M_PI * pow(raio, 2);
    cout<<"Perímetro:"<<perimetro<<endl;
    cout<<"Área:"<<area<<endl;
	return 0;
}