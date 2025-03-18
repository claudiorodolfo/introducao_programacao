public class Questao04 {
    public static void main(String[] args) {
        int[] array = {10, 5, 20, 8, 30};
        int maior = array[0];
        int menor = array[0];
        
        for (int i = 1; i < array.length; i++) {
            if (array[i] > maior) {
                maior = array[i];
            }
            if (array[i] < menor) {
                menor = array[i];
            }
        }
        
        System.out.println("Maior número: " + maior);
        System.out.println("Menor número: " + menor);
    }
}
