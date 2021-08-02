clase  Básica :
    def  __init__ ( yo ):
        pasar
    
    def  numerosN ( yo , n ):
        para  i  en el  rango ( 1 , n + 1 ):
            imprimir ( i )
            
    
    def  multiplo ( yo , numero1 , numero2 ):
        if  numero1  %  numero2  ==  0 :
            print ( "El numero {} si es multiplo de {}" . formato ( numero1 , numero2 ))
        otra cosa :
            print ( "El numero {} no es multiplo de {}" . formato ( numero1 , numero2 ))
            
    def  divisoresNumero ( self , numero ):
        lista  = []
        para  i  en el  rango ( 1 , numero + 1 ):
            si  numero  %  i  ==  0 :
                lista . añadir ( i )
        volver  lista
    
    def  primo ( yo , número ):
        contador  =  0
        para  i  en el  rango ( 1 , numero  +  1 ):
            si  numero  %  i  ==  0 :
                contador  + =  1
        si  contador  ==  2 :
            print ( "Es un numero primo" )
        otra cosa :
            print ( "No es un numero primo" )

    def  perfecto ( yo , número ):
        acu = 0
        para  i  en el  rango ( 1 , numero ):
            si  numero  %  i  ==  0 :
                acu  =  acu + i
        si  acu  ==  numero :
            imprimir ( "Numero Perfecto" )
        otra cosa :
            print ( "Numero no es perfecto" )
            
        
clase  Intermedio ( Básico ):
    def  __init__ ( yo ):
        pasar
        
    def  numerosN ( yo , n ):
        i  =  1
        mientras que  yo  <=  n :
            imprimir ( i )
            yo  =  yo  +  1
            
    def  factorial ( uno mismo , número ):
        resultado  =  1
        para  i  en el  rango ( 1 , numero  +  1 ):
            resultado  =  resultado  *  i
        volver  resultado
    
    def  fibonacci ( yo , n ):
        a  =  0
        b  =  1
        para  i  en el  rango ( n ):
            c  =  a + b
            a  =  b
            b  =  c
        devolver  un
        
    def  primosGemelos ( self , numero1 , numero2 ):
        a  =  0
        si  numero1  >  0  y  numero2  >  0  y  numero1  ! =  numero2 :
            si  numero1  >  numero2 :
                numero1 ^ = numero2
                numero2 ^ = numero1
                numero1 ^ = numero2
            para  i  en  rango ( numero1 , numero2 + 1 ):
                creciente  =  2
                esPrimo  =  Verdadero
                
                mientras  esPrimo  y  creciente  <  i :
                    si  i  %  creciente  ==  0 :
                        esPrimo  =  Falso
                    otra cosa :
                        creciente  + =  1
                si  esPrimo  y  no  un :
                    a  =  yo
                elif  esPrimo  y  a :
                    b  =  yo
                    si  b - a  ==  2 :
                        print ( "{} y {} son numeros primos gemelos" . formato ( a , b ))
                        a = yo
                    
        otra cosa :
            si  numero1  ==  numero2 :
                print ( "Incorrecto los numeros son Iguales." )    
            otra cosa :
                print ( "Los numeros son incorrectos." )
                
    def  amigos ( yo , numero1 , numero2 ):
        acu1  =  0
        lista1  = []
        para  i  en el  rango ( 1 , numero1 ):
            si  numero1  %  i  ==  0 :
                lista1 . añadir ( i )
                acu1  =  acu1  +  i
                
        acu2  =  0
        lista2  = []
        para  x  en el  rango ( 1 , numero2 ):
            si  numero2  %  x  ==  0 :
                lista2 . añadir ( x )
                acu2  =  acu2  +  x
                
        si  acu1  ==  numero2  y  acu2  ==  numero1 :
            print ( "Los numeros {} y {} si son numeros amigos." . formato ( numero1 , numero2 ))
        otra cosa :
            print ( "Los numeros {} y {} no son numeros amigos." . formato ( numero1 , numero2 ))
