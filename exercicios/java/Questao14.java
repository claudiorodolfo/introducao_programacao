import java.util.Arrays;

public class Questao14 {
    public static void main(String[] args) {
        int[] array = {5, 3, 8, 1, 2};
        
        Arrays.sort(array);  // Ordena o array
        
        System.out.println("Array em ordem crescente:");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
