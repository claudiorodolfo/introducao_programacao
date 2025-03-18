public class Questao32 {
    public static void main(String[] args) {
        int[] array = {1, 3, 5, 7, 9, 11, 13};
        int valor = 7;
        int resultado = buscaBinaria(array, valor);
        
        if (resultado != -1) {
            System.out.println("Elemento encontrado na posição: " + resultado);
        } else {
            System.out.println("Elemento não encontrado.");
        }
    }
    
    public static int buscaBinaria(int[] array, int valor) {
        int esquerda = 0;
        int direita = array.length - 1;
        
        while (esquerda <= direita) {
            int meio = (esquerda + direita) / 2;
            
            if (array[meio] == valor) {
                return meio;
            }
            
            if (array[meio] < valor) {
                esquerda = meio + 1;
            } else {
                direita = meio - 1;
            }
        }
        
        return -1;
    }
}
