public class VerificarValor {
    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50};
        int valor = 30; // Valor a ser verificado
        boolean encontrado = false;
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] == valor) {
                encontrado = true;
                break;
            }
        }
        
        if (encontrado) {
            System.out.println("O valor " + valor + " está presente no array.");
        } else {
            System.out.println("O valor " + valor + " não está presente no array.");
        }
    }
}
