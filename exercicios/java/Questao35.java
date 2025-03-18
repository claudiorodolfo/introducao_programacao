import java.util.Scanner;

public class Questao35 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Array inicial
        int[] array = {1, 2, 3, 4, 5};
        
        // Exibe o array antes da remoção
        System.out.println("Array antes da remoção:");
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // Solicita a posição do elemento a ser removido
        System.out.print("Digite a posição para remover o elemento: ");
        int posicao = scanner.nextInt();
        
        // Verifica se a posição é válida
        if (posicao >= 0 && posicao < array.length) {
            // Cria um novo array com tamanho reduzido
            int[] novoArray = new int[array.length - 1];
            
            // Copia os elementos até a posição que será removida
            for (int i = 0; i < posicao; i++) {
                novoArray[i] = array[i];
            }
            
            // Copia os elementos após a posição removida
            for (int i = posicao + 1; i < array.length; i++) {
                novoArray[i - 1] = array[i];
            }
            
            // Exibe o novo array após a remoção
            System.out.println("Array após a remoção:");
            for (int i : novoArray) {
                System.out.print(i + " ");
            }
        } else {
            System.out.println("Posição inválida.");
        }
    }
}
