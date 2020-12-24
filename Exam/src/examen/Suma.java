
public  int [] [] sum () {
    
    int [] [] m1 = {{ 1 , 2 , 4 }, { 6 , 8 , 10 }, { 2 , 5 , 3 }};
    int [] [] m2 = {{ 1 , 6 , 2 }, { 2 , 8 , 5 }, { 4 , 10 , 3 }};
    int [] [] suma =  new  int [ 3 ] [ 3 ];
     para ( int x = 0 ; x < m1 . longitud; x ++ ) {
         para ( int y = 0 ; y < m1 [x] . longitud; y ++ ) {				
         suma [x] [y] = m1 [x] [y] + m2 [x] [y];								
    }
    }
    return suma;
}
