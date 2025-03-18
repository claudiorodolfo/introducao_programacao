public class Questao11 {
    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50};
        int soma = 0;
        
        for (int i = 0; i < array.length; i++) {
            soma += array[i];
        }
        
        double media = (double) soma / array.length;
        System.out.println("A média dos elementos do array é: " + media);
    }
}
