/*
------------------------------------------------
1. Crie uma função para verificar se um ano 
inserido pelo usuário é bissexto.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>

using namespace std;

bool ehBissexto(int ano) {
    if (ano % 4 == 0)
        return true;
    else
        return false;
}

int main () {
	setlocale(LC_ALL,"Portuguese");
    int ano;
	cout<<"Informe um ano:";
    cin>>ano;

    if (ehBissexto(ano)) {
        cout<<"É bissexto";
    } else {
        cout<<"Não é bissexto";
    }
    return EXIT_SUCCESS;
}
