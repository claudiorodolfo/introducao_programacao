public class Questao03 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int[] inverso = new int[array.length];
        
        for (int i = 0; i < array.length; i++) {
            inverso[i] = array[array.length - 1 - i];
        }
        
        System.out.println("Array na ordem inversa:");
        for (int i = 0; i < inverso.length; i++) {
            System.out.println(inverso[i]);
        }
    }
}
