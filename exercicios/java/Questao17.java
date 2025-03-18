import java.util.Arrays;

public class Questao17 {
    public static void main(String[] args) {
        int[] array1 = {10, 20, 30, 40};
        int[] array2 = {10, 20, 30, 40};
        
        if (Arrays.equals(array1, array2)) {
            System.out.println("Os arrays são iguais.");
        } else {
            System.out.println("Os arrays não são iguais.");
        }
    }
}
