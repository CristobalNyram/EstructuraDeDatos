"""--------------------------------------------------------------------------------------------------------------
Listas son de tipo dinamica 

Los arreglos no pueden modificar en tiempo de ejecucion

--------------------------------------------------------------------------------------------------------"""
import sys


#esta funcion de vuelve FALSE O TRUE  si una variable es cadena o no
def valoracion(cadenaEvaluada):

    evaluacion(cadenaEvaluada.isalpha())


#esta funcion determinara si el programa funciona bien o se detiene todo
def evaluacion(valor):
    if valor == False:
       print("No digitaste un numero correcto el programa no lo puede procesar aun,gracias") 
       sys.exit() 
           
        
    else:

         print("todo marcha sin problemas")
        

  



#creamos nuestra lista 
lista = []

#lanzamos el mensaje 
cadena = input("Introduce una cadena. (--exit-- para temianar):")
valoracion(cadena)   
        


#mientras no digite la opcion de salir el programa seguira agregando datos 
while cadena != "exit":
        valoracion(cadena) #evaluamos la variable constantemente

        lista.append(cadena)#el metdo append que nos permite agregar nuevos elementos en la lista
        cadena = input("Introduce una cadena. (--exit-- para temianar):")
  

#cuando  se cumpla la anteiror condicion de ----exit--- nos mandar por defecto con el truen nos mandara al menu
while True:
    print("\n")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Darle la vuelta a la lista")
    print("6. Salir")

    #aqui recibieremos la opcion
    opcion = int(input("Dime opción:"))
    
    if opcion == 1:
        cadena = input("Introduce una cadena a buscar:")
        print("La cadena aparece %s veces" % lista.count(cadena))#"%" es usado para dar formato y fijar las variables encerradas en una "tupla" (uja lista de tamaño fijo
    
    #buscador y modfificador
    elif opcion == 2:
        cadena = input("Introduce una cadena a buscar:")
        cadenaAModificar = input("Introduce una cadena a modificar:")
        indice = 0

        #por cada elemento encontrado en la lista que concidda con nuestra cadena que introduccimos
        for elemento in lista:
            if elemento == cadena:

                #en el indice que concida con nuestra variable le daremos del valor nuevo
                lista[indice] = cadenaAModificar

            indice += 1


    elif opcion == 3:
        cadena = input("Introduce una cadena a eliminar:")
        
        #si econtramos nuestra CADENA EN nuestra LISTA entonces...
        if cadena in lista:
            #mientras la cadena que estamos buscando a remover este en nuestra lista, la borraremos
            while cadena in lista:
                lista.remove(cadena)
        else:

            #en caso de no econtralo mandale un mensaje al chencho de usuario
            print("No existe la cadena en la lista.")
    elif opcion == 4:

        
        for elemento in lista:
            print("-",elemento," ")
    
    elif opcion == 5:
        print("Ingrese de donde cambiara la lista ")
        numerador=0
        for x in range(0,len(lista)):
          print(numerador)
          print ("---"+lista[x])
          numerador += 1

        lista.reverse()
        
        print("-----------Nuevo orden---------------")
        numerador=0
      
        for x in range(0,len(lista)):
           print(numerador)
           print ("---"+lista[x])
           numerador += 1



           
        
         
    
            
   
   
    elif opcion == 6:
        print("fin de programa...gracias por usar nuestr sistema DVTECAM")
        break
    else:
        print("Opción incorrecta amiguito")





    """
    autores:Cristobal marin de los santos
            Emmanuel Evaristo
            Angel Vargas


    link de repositorio en github;        
            """    
