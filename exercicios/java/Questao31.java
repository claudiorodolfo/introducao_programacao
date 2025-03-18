public class Questao31 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        
        int primeiroElemento = array[0];
        
        for (int i = 0; i < array.length - 1; i++) {
            array[i] = array[i + 1];
        }
        
        array[array.length - 1] = primeiroElemento;
        
        System.out.println("Array após rotação para a esquerda:");
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}
