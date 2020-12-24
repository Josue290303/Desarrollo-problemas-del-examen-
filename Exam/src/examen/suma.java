package src.examen; 

public class suma {
    public static int[][] main(final String[] args) {
 
    
        final int[][] m1 = { { 1, 2, 4 }, { 6, 8, 10 }, { 2, 5, 3 } };
        final int[][] m2 = { { 1, 6, 2 }, { 2, 8, 5 }, { 4, 10, 3 } };
        final int[][] suma = new int[3][3];
     for ( int x = 0 ; x < m1 . length; x ++ ) {
         for ( int y = 0 ; y < m1 [x] . length; y ++ ) {				
         suma [x] [y] = m1 [x] [y] + m2 [x] [y];								
    }
    }
    return suma;
   }
}