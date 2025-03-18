public class Questao13 {
    public static void main(String[] args) {
        int[] arrayOriginal = {1, 2, 3, 4, 5};
        int[] arrayCopiado = new int[arrayOriginal.length];
        
        // Copiando os elementos
        for (int i = 0; i < arrayOriginal.length; i++) {
            arrayCopiado[i] = arrayOriginal[i];
        }
        
        // Imprimindo os arrays
        System.out.println("Array original:");
        for (int i = 0; i < arrayOriginal.length; i++) {
            System.out.print(arrayOriginal[i] + " ");
        }
        
        System.out.println("\nArray copiado:");
        for (int i = 0; i < arrayCopiado.length; i++) {
            System.out.print(arrayCopiado[i] + " ");
        }
    }
}
