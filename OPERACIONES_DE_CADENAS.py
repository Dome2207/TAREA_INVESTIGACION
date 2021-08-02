clase  Cadena ():
    def  __init__ ( self , cadena ):
        yo . cadena = cadena   
    def   recorrerCadena ( yo ):
        imprimir ( '_______________________________________' )
        print ( "Recorrer y presentar los datos de una cadena" )
        imprimir ( '____________________________________' )
        para  x  en  uno mismo . cadena :
            imprimir ( x , '' , end = '' )  
    def   buscarCaracter ( self , buscado ):
        imprimir ( '______________________________' )
        print ( "Buscar un carácter en una cadena" )
        imprimir ( '____________________________' )
        acum = 0
        para  x , i  en  enumerate ( self . cadena ):
            si  i ==  buscado :
                acum = acum + 1
        print ( "Su caracter se encuentra {} veces, dentro de la cadena" . formato ( acum ))
        imprimir ()  
    def   listaPosiciones ( self , caracter ):
        imprimir ( '_________________________________________________________________' )
        print ( "Retornar una lista con las posiciones dado un carácter de la cadena" )
        imprimir ( '__________________________________________________________________' )
        acum = 0
        aux = []
        para  x , i  en  enumerate ( self . cadena ):
            acum = acum + 1
            si  i  ==  caracter :
                aux . añadir ( acum )
                lista = aux
        imprimir ( lista )        
                  
    def  listaPalabras ( yo ):
        pasar  
    def  cadenaLista ( yo ):
        pasar  
    def  insertarDato ( self , buscado , posicion ):
        pasar  
    def  eliminarOcurrencias ( buscado ):
        pasar  
    def  retornaValor ( posicion ):
        pasar  
    def  concatenarCadena ( dato ):
        pasar         

cadena = 'hola como estas'
cad =  Cadena ( cadena )
# cad.recorrerCadena ()
# cad.buscarCaracter ('b')
cad . listaPosiciones ( 'v' )
