public class Questao20 {
    public static void main(String[] args) {
        String[] array = {"apple", "banana", "apple", "cherry", "apple"};
        String textoRemover = "apple";
        
        // Contando quantas ocorrências de 'textoRemover' existem
        int count = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(textoRemover)) {
                count++;
            }
        }
        
        // Criando um novo array com o texto removido
        String[] novoArray = new String[array.length - count];
        int index = 0;
        
        for (int i = 0; i < array.length; i++) {
            if (!array[i].equals(textoRemover)) {
                novoArray[index++] = array[i];
            }
        }
        
        // Imprimindo o novo array
        System.out.println("Array após remover o texto '" + textoRemover + "':");
        for (String s : novoArray) {
            System.out.print(s + " ");
        }
    }
}
