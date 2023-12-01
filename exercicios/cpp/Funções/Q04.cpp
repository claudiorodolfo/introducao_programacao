/*
------------------------------------------------
4. Crie uma função que recebe os coeficientes de
uma equação quadrática e calcula suas raízes.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>
#include <cmath>

using namespace std;

void imprimeRaizes(int a, int b, int c) {
	double delta, x1, x2;    
    delta = b*b - 4*a*c;
    if (delta > 0) {
        x1 = (-b + sqrt(delta))/(2*a);
        x2 = (-b - sqrt(delta))/(2*a); 
        cout<<"x1:"<<x1<<", x2:"<<x2<<endl;
        //x1=3, x2=2
    } else if (delta == 0) {
        x1 = (-b + sqrt(delta))/(2*a);
        cout<<"x:"<<x1<<endl;
    } else {
        cout<<"Não há raízes reais"<<endl;
    }            
}

int main () {
	setlocale(LC_ALL,"Portuguese");
	double a, b, c;
	cout<<"Informe o valor de a, b e c em: ";
    cout<<"ax^2+bx+c = 0"<<endl;
	cin>>a>>b>>c; //1 -5 6
    imprimeRaizes(a, b, c);

    return EXIT_SUCCESS;
}