public class Questao27 {
    public static void main(String[] args) {
        int N = 1000;
        System.out.println("Números perfeitos menores que " + N + ":");
        
        for (int i = 1; i < N; i++) {
            if (isPerfeito(i)) {
                System.out.print(i + " ");
            }
        }
    }
    
    public static boolean isPerfeito(int num) {
        int soma = 0;
        for (int i = 1; i < num; i++) {
            if (num % i == 0) soma += i;
        }
        return soma == num;
    }
}
