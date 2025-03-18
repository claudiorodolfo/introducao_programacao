public class Questao28 {
    public static void main(String[] args) {
        int N = 10;
        int[] fibonacci = new int[N];
        
        fibonacci[0] = 0;
        fibonacci[1] = 1;
        
        for (int i = 2; i < N; i++) {
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
        }
        
        System.out.println("Primeiros " + N + " números da sequência de Fibonacci:");
        for (int f : fibonacci) {
            System.out.print(f + " ");
        }
    }
}
