public class NumerosPrimos {
    public static void main(String[] args) {
        int N = 10;  // Número de primos desejado
        int[] primos = new int[N];
        int num = 2, count = 0;
        
        while (count < N) {
            if (isPrimo(num)) {
                primos[count] = num;
                count++;
            }
            num++;
        }
        
        System.out.println("Primeiros " + N + " números primos:");
        for (int p : primos) {
            System.out.print(p + " ");
        }
    }
    
    public static boolean isPrimo(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
