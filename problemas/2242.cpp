//Problema 2242 - Huaauhahhuahau
//https://www.urionlinejudge.com.br/judge/pt/problems/view/2242
/*
Em chats, é muito comum entre jovens e adolescentes utilizar sequências de letras, que parecem muitas vezes aleatórias, para representar risadas. Alguns exemplos comuns são:
huaauhahhuahau
hehehehe
ahahahaha
jaisjjkasjksjjskjakijs
huehuehue

Cláudia é uma jovem programadora que ficou intrigada pela sonoridade das “risadas digitais”. Algumas delas ela nem mesmo consegue pronunciar! Mas ela percebeu que algumas delas parecem transmitir melhor o sentimento da risada que outras. A primeira coisa que ela percebeu é que as consoantes não interferem no quanto as risadas digitais influenciam na transmissão do sentimento. A segunda coisa que ela percebeu é que as risadas digitais mais engra¸cadas são aquelas em que as sequências de vogais são iguais quando lidas na ordem natural (da esquerda para a direita) ou na ordem inversa (da direita para a esquerda), ignorando as consoantes. Por exemplo, “hahaha” e “huaauhahhuahau” estão entre as risadas mais engraçadas, enquanto “riajkjdhhihhjak” e “huehuehue” não estão entre as mais engraçadas.
Cláudia está muito atarefada com a análise estatística das risadas digitais e pediu sua ajuda para escrever um programa que determine, para uma risada digital, se ela é das mais engraçadas ou não.

Entrada
A entrada é composta por uma linha, contendo uma sequência de no máximo 50 caracteres, formada apenas por letras minúsculas sem acentuação. As vogais são as letras ‘a’,‘e’,‘i’,‘o’,‘u’. A sequência contém pelo menos uma vogal.

Saída
Seu programa deve produzir uma linha contendo um caractere, “S” caso a risada seja das mais engra¸cadas, ou “N” caso contrário.
*/

#include <iostream>

using namespace std;

int main() {

	char vogais[10] = {'a', 'e', 'i','o','u', 'A', 'E', 'I', 'O', 'U'};
	string risada;
	
	cin>>risada;  //exemplo de entrada: Huaauhahhuahau
	
	string risada_vogais = "";
	//loop que obtem a string passada somente com vogais
	//apos o termino do loop, risada_vogais vai ter: uaauauaau
	for (int i = 0; i < risada.size(); i++) {
		for (int j = 0; j < 10; j++) {
			if (risada[i] == vogais[j]) {
				risada_vogais = risada_vogais + risada[i];
				//risada_vogais += risada[i];
				break;
			} 
		}
	}
	//cout<<risada_vogais<<endl;
	
	//laco que verifica se a string é um palindromo, ou seja,
	//identica de tras para frente.	Por exemplo, uaauauaau, é palindromo.
	bool palindromo = true;
	for (int i = 0; i < risada_vogais.size()/2; i++) {
		int indice_inverso = (risada_vogais.size()-1) - i;	
		if (risada_vogais[i] != risada_vogais[indice_inverso]) {
			palindromo = false;
			break;
		}
	}
	
	//saida. Só imprime S, se não entrar dentro do if do bloco acima			
	if (palindromo)	{	
		printf("S\n");
	}  else {
		printf("N\n");
	}
}
