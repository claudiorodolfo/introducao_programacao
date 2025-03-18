public class Questao23 {
    public static void main(String[] args) {
        int[] array1 = {1, 2, 3};
        int[] array2 = {4, 5, 6};
        int[] novoArray = new int[array1.length + array2.length];
        
        System.arraycopy(array1, 0, novoArray, 0, array1.length);
        System.arraycopy(array2, 0, novoArray, array1.length, array2.length);
        
        System.out.println("Novo array combinado:");
        for (int i : novoArray) {
            System.out.print(i + " ");
        }
    }
}
