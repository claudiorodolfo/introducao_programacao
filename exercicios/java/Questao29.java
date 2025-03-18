public class Questao29 {
    public static void main(String[] args) {
        int N = 10;
        int[] lucas = new int[N];
        
        lucas[0] = 2;
        lucas[1] = 1;
        
        for (int i = 2; i < N; i++) {
            lucas[i] = lucas[i - 1] + lucas[i - 2];
        }
        
        System.out.println("Primeiros " + N + " números da sequência de Lucas:");
        for (int l : lucas) {
            System.out.print(l + " ");
        }
    }
}
