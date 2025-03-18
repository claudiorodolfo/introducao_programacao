public class Questao05 {
    public static void main(String[] args) {
        int[] array = {10, 20, 4, 30, 25};
        int segundoMaior = Integer.MIN_VALUE-1;
        int maior = Integer.MIN_VALUE;

        for (int i = 0; i < array.length; i++) {
            if (array[i] > maior) {
                segundoMaior = maior;
                maior = array[i];
            } else if (array[i] > segundoMaior 
					&& array[i] != maior) {
                segundoMaior = array[i];
            }
        }
        System.out.println("Segundo maior número: " + segundoMaior);
    }
}
