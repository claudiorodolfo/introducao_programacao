#include <iostream>
#include <clocale>
#include <string>
#include <cctype>	//para tolower e toupper

using namespace std;

int main() {
	setlocale(LC_ALL,"Portuguese");
	string nome = "Instituto Federal da Bahia";
	
    for (int i = 0; i < nome.size(); i++)
        nome[i] = toupper(nome[i]);
	cout<<"Ma�usculo: "<<nome<<endl;
	    
    for (int i = 0; i < nome.size(); i++)
        nome[i] = tolower(nome[i]);
	cout<<"Min�sculo: "<<nome<<endl;
	
    return 0;
}
