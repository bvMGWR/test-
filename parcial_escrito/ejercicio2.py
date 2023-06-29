


"""Se solicita:
A) Crear una función para encontrar la palabra que tiene más caracteres de la lista a
B) Crear una función para encontrar la palabra que tiene menos caracteres de la lista b
C) Crear una función que concatene ambas listas
D) Crea una función que transforme los elementos de la lista en Mayúsculas.
E) Crear una función y ordenar la lista de forma alfabética."""


a = ["Rojo", "Verde", "Celeste", "Violeta"]
b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]

def mas_larga(lista):
   
    palabra = ""
    for i in lista:
        if len(i) > len(palabra):
            palabra = i
    return palabra

def mas_corta(lista):
   
    palabra = lista[0]
    for i in lista:
        if len(i) < len(palabra):
            palabra = i
    return palabra

def concatenar(lista,lista2): 
   resul= lista + lista2
   return resul 

def mayusculas(lista):
   tex= str(lista)
   may= tex.upper()
   return may

def ordenar(lista): 
    lista.sort()
    return lista
  

 
print("La palabra más larga en la lista 'a' es:", mas_larga(a))
print("La palabra más corta en la lista 'b' es:", mas_corta(b))
print(concatenar(a,b))
print(mayusculas(a))
print(ordenar(a))
