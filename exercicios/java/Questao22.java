public class Questao22 {
    public static void main(String[] args) {
        char[] array = {'a', 'b', 'c', 'e', 'i', 'o', 'u'};
        int count = 0;
        
        for (char c : array) {
            if (isVogal(c)) {
                count++;
            }
        }
        
        System.out.println("Número de vogais no array: " + count);
    }
    
    public static boolean isVogal(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
