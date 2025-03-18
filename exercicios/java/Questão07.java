public class Questão07 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6};
        int soma = 0;
        
        for (int i = 0; i < array.length; i++) {
            if (i % 2 == 0) {  // Índices pares
                soma += array[i];
            }
        }
        
        System.out.println("Soma dos elementos nas posições pares: " + soma);
    }
}
