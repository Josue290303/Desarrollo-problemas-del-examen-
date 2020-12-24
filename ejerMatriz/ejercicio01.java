 public  static  void  main ( String [] args ) {
        // Lógica de aplicación de código TODO aquí
         Matrices mt = nuevas  Matrices ();
         mt . ia . imprimirMatriz (mt . transformada33 ( 5 , 0 ));
    }
    
    impArr ia = nuevo impArr ();

public  int [] [] transformada01 ( int  dimen , int  numInit ) {
    int [] [] matriz = new  int [dimen] [dimen];
    int item = 0 ;
    para ( int fila = 0 ; fila < dimen; fila ++ ) {
        para ( int columna = 0 ; columna < dimen; columna ++ ) {
            si (columna < dimen - fila) {
            item = numInit + (fila + columna) * (fila + columna + 1 ) / 2  + fila;
            matriz [fila] [columna] = artículo;                
            }
        }
    }
    matriz de retorno ;
}