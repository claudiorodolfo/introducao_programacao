public class Questao21 {
    public static void main(String[] args) {
        char[] array = {'a', 'b', 'c', 'e', 'i', 'o', 'u'};
        
        for (int i = 0; i < array.length; i++) {
            if (isVogal(array[i])) {
                array[i] = '*';
            }
        }
        
        System.out.println("Array após substituir as vogais por asteriscos:");
        for (char c : array) {
            System.out.print(c + " ");
        }
    }
    
    public static boolean isVogal(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
