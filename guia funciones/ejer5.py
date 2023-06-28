numeros = []

while True:
    numero = int(input("Ingrese un número entero positivo (o -1 para salir): "))
    
    if numero == -1:
        break
        
    if numero > 0:
        numeros.append(numero)


def promedio(lista): 
    a= len(lista)
    b=sum(lista)
    prom= b/a
    return prom
def suma_par(lista): 
    suma_par=0
    for i in lista: 
        if i % 2 ==0: 
            suma_par= suma_par + i
    return suma_par

def suma_inpar(lista): 
    suma_inpar=0
    for i in lista: 
        if i % 2 !=0: 
            suma_inpar= suma_inpar + i
    return suma_inpar

print("la lista ingresada es:",numeros)
print("la suma de los pares es:", suma_par(numeros))
print("la suma de los inpares es:", suma_inpar(numeros))
print("la suma total es:",sum(numeros))
print("el promedio es", promedio(numeros))
print("el numero mayor es: ", max(numeros))