/*
------------------------------------------------
18. Crie um algoritmo/fluxograma/programa que 
dados os valores de a, b e c referentes a 
equação de segundo grau, ax2 + bx + c = 0, 
forneça as raízes dessa equação. Considere que
os valores de a, b, c sempre geraram um delta 
positivo. 
Usar a biblioteca cmath.
 */
#include <iostream>
#include <cmath>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	double a, b, c, delta, x1, x2;
	cout<<"Informe o valor de a em: ";
    cout<<"ax^2+bx+c = 0"<<endl;
	cin>>a; //1
	cout<<"Informe o valor de b em: ";
    cout<<"ax^2+bx+c = 0"<<endl;
	cin>>b; //-5
	cout<<"Informe o valor de c em: ";
    cout<<"ax^2+bx+c = 0"<<endl;
	cin>>c; //6       
    delta = b*b - 4*a*c;
    x1 = (-b + sqrt(delta))/(2*a);
    x2 = (-b - sqrt(delta))/(2*a);    
    cout<<"x1:"<<x1<<" x2:"<<x2<<endl;
    //x1=3, x2=2
	return 0;
}