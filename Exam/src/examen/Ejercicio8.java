package src.examen;

import src.matriz.ImprimirArreglos;

public class Ejercicio8 {
    public static void main(String[] args) {
        
         Ejercicio8 mt=new Ejercicio8(); 
         mt.ia.imprimirMatriz(mt.transformada08(5, 0));
    }
    ImprimirArreglos ia= new ImprimirArreglos();
   public int[][] transformada08(int dimen, int numInit){
    int[][] matriz=new int[dimen][dimen];
    
    for(int fila=0; fila<matriz.length;fila++){ //4
        for(int columna=0; columna<matriz.length;columna++){ //matriz[0].length-1
            if(columna>=fila){                            
                matriz[fila][columna]= numInit;                                                                
                numInit++;
                
            }else{
               matriz[fila][columna]=-1; 
            }
        }
        
    }
    return matriz;
 }
}