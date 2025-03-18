import java.util.Scanner;

public class Questao02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor de N: ");
        int N = scanner.nextInt();
        
        int[] quadrados = new int[N];
        for (int i = 0; i < N; i++) {
            quadrados[i] = Math.pow(i+1, 2);
        }
        
        System.out.println("Quadrados dos números de 1 a " + N + ":");
        for (int i = 0; i < quadrados.length; i++) {
            System.out.println((i+1) +"\t" + quadrados[i]);
        }
    }
}
