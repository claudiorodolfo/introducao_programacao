public class Questao33 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3};
        int novoElemento = 4;
        
        int[] novoArray = new int[array.length + 1];
        
        for (int i = 0; i < array.length; i++) {
            novoArray[i] = array[i];
        }
        
        novoArray[array.length] = novoElemento;
        
        System.out.println("Array antes da adição:");
        for (int i : array) {
            System.out.print(i + " ");
        }
        
        System.out.println("\nArray após a adição:");
        for (int i : novoArray) {
            System.out.print(i + " ");
        }
    }
}
