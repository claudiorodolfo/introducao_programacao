public class Questao06 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int soma = 0;
        
        for (int i = 0; i < array.length; i++) {
            soma += array[i];
        }
        
        System.out.println("Soma de todos os elementos: " + soma);
    }
}
