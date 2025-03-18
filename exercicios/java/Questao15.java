import java.util.Arrays;
import java.util.Collections;

public class Questao15 {
    public static void main(String[] args) {
        Integer[] array = new Integer[10];
        
        // Preenchendo o array com números aleatórios
        for (int i = 0; i < array.length; i++) {
            array[i] = (int) (Math.random() * 100);  // Números aleatórios de 0 a 99
        }
        
        System.out.println("Array antes de ordenar:");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        
        // Ordenando o array em ordem decrescente
        Arrays.sort(array, Collections.reverseOrder());
        
        System.out.println("\nArray após ordenar de forma decrescente:");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
