import java.util.Scanner;

public class Questao24 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int[] array = {10, 20, 30, 40};
        System.out.print("Digite a posição para inserir o elemento: ");
        int posicao = scanner.nextInt();
        System.out.print("Digite o elemento a ser inserido: ");
        int elemento = scanner.nextInt();
        
        if (posicao >= 0 && posicao <= array.length) {
            int[] novoArray = new int[array.length + 1];
            
            for (int i = 0; i < posicao; i++) {
                novoArray[i] = array[i];
            }
            
            novoArray[posicao] = elemento;
            
            for (int i = posicao; i < array.length; i++) {
                novoArray[i + 1] = array[i];
            }
            
            System.out.println("Novo array após inserção:");
            for (int i : novoArray) {
                System.out.print(i + " ");
            }
        } else {
            System.out.println("Posição inválida.");
        }
    }
}
