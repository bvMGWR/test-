#palabra recervada def, para definir una funcion 
def mi_primera_funcion(): 
    print("esta es mi primera funcion")

#para tareas especificas 

mi_primera_funcion()

#convinar una funcion con listas, concatenar #parametros, argumentos 
#retrum retornar, que va a devolver, en este caso devuelve la concatenacion de la lista 1 y lista2 

def concatenar(lista1, lista2):
    return lista1 + lista2

#scope local engloba, las listas van despues fuera de la funcion 

lista1 = [1,2,3]
lista2= [4,5,6]

#concatenar(), tenemos que darle parametros, argumentos que serian las listas
print(concatenar(lista1, lista2))

#si pasamos el mous sobre la funcion, puede darnos any o none, any significa que necesita parametros y none nada 

def multiplicacion (num1,num2): 
    return num1 * num2
#multiplicacion() hay que darle argumentos 
print(multiplicacion(10,2))
print(multiplicacion(5,5))

#funcion duma y resta por teclado 
def suma (a, b):
    return a+b

def resta (a,b): 
    return a - b

a= int(input("ingrese el valor de a; *"))
b= int(input("ingrese el valor de b; *"))

#se llama a la funcion suma 

resultado= suma (a,b)
print("la suma es de:", resultado)
resultado2= resta (a,b)
print("la resta es de:", resultado2)

