#include <iostream>
#include <clocale>
#include <string>

using namespace std;

int main() {
	setlocale(LC_ALL,"Portuguese");	
	string nome = "Instituto Federal da Bahia";
	cout<<"em "<<nome<<" h� ";
	cout<< nome.size() <<" caracteres."<<endl;
    return 0;
}
