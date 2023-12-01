#include <iostream>

using namespace std;

int main() {
   string nome;
   int idade;
   float altura;

   cout<<"Informe um nome, idade e altura ";
   cout<<"separados por espaço:"<<endl;
   cin>>nome>>idade>>altura;
   cout<<nome<<" tem "<<idade<<" anos ";
   cout<<"e mede "<<altura<<" metros."<<endl;	

	return 0;
}