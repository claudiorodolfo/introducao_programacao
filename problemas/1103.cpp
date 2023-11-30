//1103 - Alarme Despertador
//https://www.urionlinejudge.com.br/judge/pt/problems/view/1103

/*
Daniela é enfermeira em um grande hospital, e tem os horários de trabalho muito variáveis. Para piorar, ela tem sono pesado, e uma grande dificuldade para acordar com relógios despertadores.
Recentemente ela ganhou de presente um relógio digital, com alarme com vários tons, e tem esperança que isso resolva o seu problema. No entanto, ela anda muito cansada e quer aproveitar cada momento de descanso. Por isso, carrega seu relógio digital despertador para todos os lugares, e sempre que tem um tempo de descanso procura dormir, programando o alarme despertador para a hora em que tem que acordar. No entanto, com tanta ansiedade para dormir, acaba tendo dificuldades para adormecer e aproveitar o descanso.
Um problema que a tem atormentado na hora de dormir é saber quantos minutos ela teria de sono se adormecesse imediatamente e acordasse somente quando o despertador tocasse. Mas ela realmente não é muito boa com números, e pediu sua ajuda para escrever um programa que, dada a hora corrente e a hora do alarme, determine o número de minutos que ela poderia dormir.

Entrada
A entrada contém vários casos de teste. Cada caso de teste é descrito em uma linha, contendo quatro números inteiros H1 , M1 , H2 e M2, com H1:M1 representando a hora e minuto atuais, e H2:M2 representando a hora e minuto para os quais o alarme  despertador foi programado (0≤H1≤23, 0≤M1≤59, 0≤H2≤23, 0≤M2 ≤59).
O final da entrada é indicado por uma linha que contém apenas quatro zeros, separados por espaços em branco.

Saída
Para cada caso de teste da entrada seu programa deve imprimir uma linha, cada uma contendo um número inteiro, indicando o número de minutos que Daniela tem para dormir.
*/

#include <iostream>
 
using namespace std;
 
int main() {

	/* 
	Usa-se linha != "0 0 0 0" para questoes onde o fim do teste eh determinado por valores zero
	Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
	*/

    int h1, m1, h2, m2;
    cin>>h1>>m1>>h2>>m2;
	
	while (!((h1 == 0) && (m1 == 0) && (h2 == 0) && (m2 == 0))) {
	//while ((h1 != 0) || (m1 != 0) || (h2 != 0) || (m2 != 0)) {
		
		/*
		calcula a quantidade de minutos entre dois horarios
		caso a hora final seja menor que a inicial
		ou a hora inicial seja igual final e o minuto final seja menor que o inicial
		*/
		if ((h1 > h2) || (h1 == h2 && m1 > m2)) {
			h2 += 24;
		}

		//converte horas em minutos
		h1 *= 60;
		h2 *= 60;

		//soma as horas convertidas em minutos com os minutos
		int r1, r2;
		r1 = h1 + m1;
		r2 = h2 + m2;

		//calcula a quantidade de minutos
		cout<<r2 - r1<<endl;

		cin>>h1>>m1>>h2>>m2;
	}
    return 0;
}
