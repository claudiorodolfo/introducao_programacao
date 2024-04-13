#include <iostream>
#include <clocale>
#include <cmath>

using namespace std;

int main() {
	setlocale(LC_ALL,"Portuguese");
    float imc, peso, altura;
    count<<"Informe o peso (kg) e a altura(m):";
    cin>>peso>>altura;
    imc = peso/ pow(altura, 2);
    cout<<"IMC:"<<imc<<endl;
    return 0;
}
