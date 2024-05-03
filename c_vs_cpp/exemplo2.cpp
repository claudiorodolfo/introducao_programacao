#include <iostream>

int main() {
   std::string nome;
   int idade;
   float altura;

   std::cout<<"Informe um nome, idade e altura ";
   std::cout<<"separados por espaço:"<<std::endl;
   std::cin>>nome>>idade>>altura;
   std::cout<<nome<<" tem "<<idade<<" anos ";
   std::cout<<"e mede "<<altura<<" metros."<<std::endl;

   return 0;
}
