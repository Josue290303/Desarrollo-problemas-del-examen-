package src.matriz; 
public class ImprimirArreglos {
     public  void imprimirVector(final Object[] vector) {
         for (int indice = 0; indice < vector.length; indice++) {
             System.out.println(vector[indice]);
         }
     }

     public void imprimirVector(final int[] vector) {
         for (int indice = 0; indice < vector.length; indice++) {
             System.out.println(vector[indice]);
         }
     }

     public void imprimirMatriz(final Object[][] matriz) {
         for (int filaSubInd = 0; filaSubInd < matriz.length; filaSubInd++) {
             for (int columSubInd = 0; columSubInd < matriz[0].length; columSubInd++) {
                 System.out.print(matriz[filaSubInd][columSubInd] + "\t");
             }
             System.out.println();
         }
     }

     public void imprimirMatriz(final int[][] matriz) {
        for(int filaSubInd=0; filaSubInd<matriz.length;filaSubInd++){
            for(int columSubInd=0; columSubInd<matriz[0].length;columSubInd++){
                System.out.print(matriz[filaSubInd][columSubInd]+"\t");
            }
            System.out.println();
        }
    }    
}