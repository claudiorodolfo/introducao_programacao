/*
------------------------------------------------
15. Crie um algoritmo/fluxograma/programa que 
leia o preço de um produto e escreva o valor de
venda final dele. O vendedor quer vendê-lo com 
40% de lucro se o valor da compra for menor que
R$20,00; caso contrário, o lucro será de 30%.
 */
#include <iostream>
#include <clocale>

using namespace std;
int main () {
	setlocale(LC_ALL,"Portuguese");
	float preco, venda;
	cout<<"Informe o preço:";
	cin>>preco;

    if (preco < 20.0)
        venda = preco * 1.4;
    else 
        venda = preco * 1.3;
    
    cout<<"Preço de Venda:"<<venda;
	return 0;
}