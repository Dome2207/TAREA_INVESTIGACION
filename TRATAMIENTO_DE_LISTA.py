clase  TratamientoListas ():
    
    def  __init__ ( self , lista , diccionario , tupla ):
        yo . lista = lista
        yo . diccionario = diccionario
        yo . tupla = tupla

    def  PresentarLista ( yo ):
        print ( "Recorrer y presentar los datos de una lista" )
        para la  lista  en  sí mismo . lista :
            imprimir ( lista , fin = '' )
        imprimir ()
        
    
    def  buscarLista ( self , buscado ):
        print ( "Buscar un valor en una lista" )
        enc = Falso
        para  POS , ele  en  enumerate ( auto . Lista ):
            if  ele == buscado :
                enc = Verdadero
                pausa
        si  enc == Verdadero :
           print ( "Su valor si se encuentra en la lista, se encuentra en la posicion: {}" . format ( pos ))
        otra cosa :
            print ( "Su valor no se encuentra en la lista" )

    
    def  ListaFactorial ( self ):
        print ( "Retornar una lista con los factoriales" )
        para  POS , i  en la  enumeración ( auto . Lista ):
            si  i  > =  0 :
                acu = 1
                para  num  en  rango ( i , 1 , - 1 ):
                    acu  = acu * num
                print ( "numero: {}, Factorial: {}" . formato ( i , acu ))
        imprimir ()           
    
    def  listaPrimo ( yo ):
        print ( "Retornar una lista de números primos" )
        para  POS , i  en la  enumeración ( auto . Lista ):
            si  i  > =  0 :
                primo = Verdadero
                divisor = 2
                while  divisor  <  i  y  primo  == True :
                    Res =  i % divisor
                    si  Res  ==  0 :
                        primo + = 1
                    divisor + = 1
                si  primo  == Verdadero :
                    print ( "Numero" , i , "es primo" )
                otra cosa :
                    print ( "Numero" , i , "no es primo" )
            otra cosa :
                print ( "Su lista contiene numeros y letras" )    
        imprimir ()
    
    def  listaNotas ( self , listaNotasDicccionario ):
        print ( "Recorrer una lista de diccionario con notas de alumnos" )
        para  nom  en  listaNotasDicccionario :
            para  clave , valor  en  nom . elementos ():
                print ( clave , ":" , valor , end = "" )
            imprimir ()
  
    
    def  insertarLista ( self , valor , posicion ):
        print ( "Insertar un dato en una Lista dada la Posición" )
        imprimir ()
        auxlista = []        
        para  POS , ele  en  enumerate ( auto . Lista ):
            si  valor  <  ele :
                pausa
        para  i  en  rango ( posicion ):
            auxlista . append ( auto . Lista [ i ])
        auxlista . añadir ( valor )

        para  j  en  gama ( posicion , len ( auto . Lista )):
            auxlista . append ( auto . Lista [ j ])
        yo . lista = auxlista
        volver a  sí mismo . lista
  
    
    def  eliminarLista ( self , lista ):
        print ( "Eliminar todas las ocurrencias en una Lista" )
        imprimir ()
        lista2  = {}
        para  yo  en la  lista :
            Si  i  en  lista2 :
                lista2 [ i ] + =  1
            otra cosa :
                lista2 [ i ] =  1 
        print ( "Queda lo siguiente:" , lista2 )
        print ( "En total son {} elementos sin contar las repeticiones" . format ( len ( lista2 )))
        lista3  = []        
        para  clave , valor  en  enumerate ( lista2 ):
            lista3 . añadir ( valor )
        volver ( lista3 )   

    def  retornaValorLista ( self , lista ):
        print ( "Retornar cualquier valor de una lista eliminándolo" )
        imprimir ()
        n = int ( input ( "que valor quieres eliminar:" ))      
        para  x , i  en  enumerate ( lista ):
            si  i  ==  n :
                del  lista [ x ]  
        volver ( lista )

  
    def  copiarTuplaLista ( self ):
        print ( "Copiar cada elemento de una tupla en una lista" )
        aux1 = lista ( auto . tupla )
        volver  aux1      
  
    
    def  vueltoLista ( self , listaClientesDiccionario ):
        print ( "Dar el vuelto a varios clientes" )
        pasar
        
         
pos = 2
diccionario = [{ 'nombre' : 'jefferson' , 'nota' : 90 }, { 'nombre' : 'carlos' , 'nota' : 80 }, { 'nombre' : 'luisa' , 'nota' : 90 } ]
lista = [ - 2 , - 2 , 5 , 3 , 40 , 50 ]
tupla = ( 22 , 23 , 24 , 25 )
listaClientesDiccionarios = [{ 'cliente' : 'jefferson' , 'deuda' : 90 }, { 'cliente' : 'carlos' , 'deuda' : 80 }, { 'cliente' : 'robert' , 'deuda' : 50 } ]
ord1 =  TratamientoListas ( lista , diccionario , tupla )
ord1 . PresentarLista ()
# rd1.buscarLista (40)
# ord1.ListaFactorial ()
# ord1.listaPrimo ()
# ord1.listaNotas (diccionario)
# imprimir (ord1.insertarLista (600,5))
# imprimir()
# lista1 = []       
# num = int (input ("Cuantos elementos desea en la lista ?:"))
# para x en el rango (num):
# valor = int (input ("Ingrese el elemento:")) 
# lista1.append (valor)
# aux = lista1
# imprimir (ord1.eliminarLista (aux))
# lista2 = []       
# num = int (input ("Cuantos elementos desea en la lista ?:"))
# para x en el rango (num):
# valor = int (input ("Ingrese el elemento:")) 
# lista2.append (valor)
# aux = lista2
# imprimir (ord1.retornaValorLista (aux))
#print (ord1.copiarTuplaLista ())
#print (ord1.vueltoLista (listaClientesDiccionarios))
