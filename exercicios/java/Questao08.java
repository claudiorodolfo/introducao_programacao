public class Questao08 {
    public static void' main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int multiplicador = 2;
        
        System.out.println("Array antes da multiplicação:");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        
        System.out.println("\nArray depois da multiplicação:");
        for (int i = 0; i < array.length; i++) {
            array[i] *= multiplicador;
            System.out.print(array[i] + " ");
        }
    }
}
