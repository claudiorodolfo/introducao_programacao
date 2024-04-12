#include <iostream>
#include <clocale>
#include <cmath>

using namespace std;

int main() {
    float imc, peso, altura;
    count<<"Informe o peso e a altura:";
    cin>>peso>>altura;
    imc = peso/ pow(altura,2);
    cout<<"IMC:"<<imc;
    return 0;
}