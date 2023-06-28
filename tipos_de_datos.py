#datos 
edad= 18
estatura = 1.60
peso = 70.5 #real
complejo= 1 + 4j #complejo 
#float numero 
print ("trasformando un valor entero a real:", float (edad))
#operacion aritmetica basica 
imc = peso/ (estatura**2)
#salto de linea \n
print ("mi imc es de:" ,imc, "\n")
#{:.2F} 2 decimales 
print ("mi imc es de {:.2f} ".format (imc),"\n")
#02 DATOS DE TIPO CADENA DE CARACTERES solo las variables con palabras se les pone comillas 
asignatura= "progrmacion"
carrera= "ingenieria civil informatica" 
print ("la asignatura de", asignatura,"corresponde a la carrera de",carrera )
#para contar la cantidad de carctares 
print ("la cantidad de caracteres de la palabra",asignatura, "es de:" ,len(asignatura))
#valores booleanos 
ampolleta= False
interruptor= True
print (ampolleta, interruptor)
#type tipos de datos con los que trabajamos 
print ( "la variable ampolleta es de tipo:" ,type (interruptor), "\n")
#podemos trasformar cualquier valor en un booleano tipo de dato verdadero y falso
print (bool (0))
print (bool (None))
print (bool (True))
#listas para guardar varios valores en una variable
#inicializar una lista 
nueva_lista = list()
otra_lista = []
print("esta es la lista vacia",nueva_lista)
print ("esta es otra lista vacia:",otra_lista)
print (type(otra_lista))
#declarando nuevas listas con corcchetes 
estudiantes= ["matias", "marcos", "cristobal", "sebastian", "marcos"]
num= [1,2,3,4,5,6,1]
leguaje= ["python"]
#lista de estructuras diferentes 
data= ["osorno", {"UV:" "bajo nivel", 'tem"C'}], (-40.5783, -73.1553)
lista_mixta= ["marcela", 100, True]
print ("lista de carcteres:" ,estudiantes)
print ("lista de numeros:",num)
print ("lista de elementos",leguaje)
print ("esta es una lista mixta:",lista_mixta)
print ("esto igual es una lista", data ) 
print (len(lista_mixta)) #para saber la cantidad de carcteres 
#para saber si se repite 
print (estudiantes.count ("marcos"))
print (estudiantes.count("matias"))
print (num.count (1))
print (num.count (5000)) #numero que no esta en la lista
#len cuenta las letras count cuneta cuntas veces se rpite un elemento
#como especifico algo en una lista 
#se comienza a contar desde el 0,1,2 indice, pocision, index
#marca error si nos pasamos del limite de indice 
print (estudiantes [0])
print (estudiantes[4])
#con negativos cuenta al reves -4,-3,-2,-1. comenzando desde el ultimo 
print (estudiantes [-2])  
#se pueden sumar listas 
print(list(range(20))) #genera el numero de elementos 
print(list(range(1,5)))
#tuplas (no mutables)
newtupla =tuple()
grupo1 = ("daniel","cristian", "felipe", 100 , 2000, "daniel")
#tpye tipo de dato con el que trabajamos 
#index me muestra la posicion del elemento buscado 
print ("indice del elemento", grupo1.index ("daniel"))
#reasignado el primer elemento de la tupla, no se puede modificar dara error
#grupo1 [0]= "constanza"
#print (grupo1)
#¿se pueden sumar las tuplas?
# obteniendo un trozo de tupla 
grupo2= ("pedro",100," felipe",200, "diego", 2022 )
print ("trozo de la tupla", grupo2[0:3])
#entonces como se puede modificar una tupla? 
grupo1= list(grupo1)
print ("la tupla ahora es de tipo", type(grupo1),)
#sets (conjuntos)estructura fija 
#formas de inicializar un sets 
conjunto_vacio= set()
conjunto_vacio1= {} #diccionario o sets 
print (type (conjunto_vacio))
conjunto_colores= set ({"azul", "rojo","verde"})
conjunto_animales= ({"gato", "perro", "loro"})
print (type(conjunto_colores)) #tipo de dato set 
print (type(conjunto_animales)) #tipo de dato set 
print ("el siguiente set tiene los siguientes colores:",conjunto_colores)
print ("el siguiente set tiene los siguientes animales:",conjunto_animales)
#no es posible encontrar la localizacion de un concepto en los set 
#se pueden agregar mas datos con .add
conjunto_colores.add ("celeste")
print ("el siguiente set tiene los siguientes colores:",conjunto_colores)
#las listas son mutables las tuplas no 
#se puede tener lista dentro de otras listas 
#las carcateristicas de las tuplas conexion de datos ordenados, con index, no se pueden modificar, 
#tupla inmutabe con lista dentro, pueden tener diferentes tipos de elemetos y son mas eficientes 
#index arroja la posicion en las tuplas
#los set son un conjuntos no ordenados de datos set() o {}
#list() o []
#tupla ()
#diccionario con {}
#CLAVE unica para un elemento 
dicionario1= dict()
diccionario2= {}
datos_personales= {
"nombre": "barbara",
"institucion": "ulaagos",
"edad": 18,
"asignatura" : {"estructuras de datos", "programacion"}
}
#para consultar hay que saber el nombre de la clave
#len, cuantos elementos hay, son 4 claves y elementos 
print (len(datos_personales))
print (datos_personales["nombre"]) 
#agregar un nuevo dato 
datos_personales["cuidad"] = "osorno"
#para borrar un datos del 
print (datos_personales)
del datos_personales ["cuidad"]
Nombre= input("¿cual es tu nombre?")
edad= input ("¿cual es tu edad?")
print (type(edad))
Total_edad= int(edad) + 20
print ("hola mi nombre es", Nombre, "tengo", edad, "años" "y en 20 años tendre",Total_edad,"años")

#al pedir edad input lo guarda como cadena de texto por lo que hay que usar la funcion type para trasformalo y int 

#tipas set listas y dicionarios
#modulo, resto cosiente elevado
#t= timepo g=gravedad v=velocidad/fisica 
g= 14
t=60
v= g *t 
#format
c2= complex (3,-5)
print (c2.real)#el tre sera real 
print (c2.imag)#5 imaginario 
print ("hola" *5)
#print ("hola" * 3.5*2)
print ("hola" * (int(5)))
#operadored de comparacion 
#print (a==b) #comparacion 
#print (a != b) #desigualdad 
#print (a==b) 
#al imprimirlo dara un booleano 
#print (a==b) #comparacion 
#codigo ascii le otorga valores numericos a las letras 
#operadores logicos y/O 
#ELIF SINO SI indentar el codigo 
#iteraciones cuando se repite un bucle osea 1, 2 veces

