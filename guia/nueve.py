#lista de numeros enteros 
numeros= [4,3,8, 12, 6, 10, 14, 3, 6]
#eliminar el ultimo elemento de la lista 
numeros.pop()
print(numeros)
#agrega en la primera posicion el numero 2 
numeros.insert(0,2)
print(numeros)
#elimina los numeros duplicado de la lista 
print(numeros.count(3))
print (numeros.pop())
print (numeros)
print (len(numeros))
a=(len(numeros))#cuenta la cantidad caracteres de la lista
print(sum(numeros))
b=(sum(numeros))#suma los numeros de una lista 
media= b/a
print(media)
#redonda a un numero especifico de deccimales
print(round(media,1))
#ORDENA LA LISTA DE FORMA ASENDENTE 
print(numeros.sort())
print (numeros)
#index para saber en que pocision se encuntra en una lista
#print(numeros.index(6))
#print(numeros.index(8))
print(numeros[3])
print(numeros[4])
#para sacr la mediana cuando de una lista par se deben sumar los 2 numeros del centro y divir en 2 el resultado
m= (numeros[3]) + (numeros[4])
print(m)
mediana= m/2
print(mediana)
