public class Questao10 {
    public static void main(String[] args) {
        int[] array = {-1, 2, -3, 4, -5};
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] < 0) {
                array[i] = 0;
            }
        }
        
        System.out.println("Array após substituir negativos por zero:");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
