/*
------------------------------------------------
5. Crie uma função para calcular a distância 
entre dois pontos em um plano cartesiano. As 
coordenadas x, y de cada ponto devem ser 
inseridas pelo usuário.
 */
#include <iostream>
#include <clocale>
#include <cstdlib>
#include <cmath>

using namespace std;

float distancia(float x1, float y1, float x2, float y2){
    return sqrt(pow(x1-x2,2) + pow(y2-y1,2));
}

int main () {
    setlocale(LC_ALL,"Portuguese");
    cout<<"A distancia é:"<<distancia(6,8,9,4);
    //5
    return EXIT_SUCCESS;
}