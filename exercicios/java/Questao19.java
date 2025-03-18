public class Questao19 {
    public static void main(String[] args) {
        String[] array = {"A", "B", "C", "D"};
        
        System.out.println("Array antes de inverter:");
        for (String s : array) {
            System.out.print(s + " ");
        }
        
        // Invertendo o array
        for (int i = 0; i < array.length / 2; i++) {
            String temp = array[i];
            array[i] = array[array.length - 1 - i];
            array[array.length - 1 - i] = temp;
        }
        
        System.out.println("\nArray após inverter:");
        for (String s : array) {
            System.out.print(s + " ");
        }
    }
}
