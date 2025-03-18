public class Questao25 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 2, 1};
        boolean isPalindromo = true;
        
        for (int i = 0; i < array.length / 2; i++) {
            if (array[i] != array[array.length - 1 - i]) {
                isPalindromo = false;
                break;
            }
        }
        
        if (isPalindromo) {
            System.out.println("O array é um palíndromo.");
        } else {
            System.out.println("O array não é um palíndromo.");
        }
    }
}
