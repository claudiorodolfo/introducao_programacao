public class Questao16 {
    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50};
        int valor = 30;
        int indice = -1;
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] == valor) {
                indice = i;
                break;
            }
        }
        
        System.out.println("Índice da primeira ocorrência do valor " + valor + ": " + indice);
    }
}
