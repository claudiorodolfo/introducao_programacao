import java.util.HashSet;

public class Questao30 {
    public static void main(String[] args) {
        int[] array = {1, 2, 2, 3, 4, 4, 5};
        HashSet<Integer> set = new HashSet<>();
        
        for (int i : array) {
            set.add(i);
        }
        
        System.out.println("Array após remover os elementos repetidos:");
        for (int num : set) {
            System.out.print(num + " ");
        }
    }
}
