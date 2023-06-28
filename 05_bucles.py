edad= 15 
num= 0 
#bucle infinito 
'''while edad < 18: 
    print("eres menor de edad no puedes manejar")'''
#while True: 
num= 0 
while num >= 100:
    print(num)
    num +=2
print("primer bucle terminado")

while num >= 200:
    print(num)
    num +=2
else: 
    print ("mi condicion es igual o mayor a 200")
print("segundo bucle cerrado\n")



while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("mi condicion es igual a 250")

print("tercer bucle cerrado \n")

#ahi no imprime el if proque esta fuera, en el caso del else si es necesario que este fuera 
'''while num <= 300:
    print(num)
    num += 2
 if num == 250:
        print("mi condicion es igual a 250")'''
#while y break 
while num <= 400:
    print(num)
    num += 2
    if num == 350 :
        print("se detiene la ejecucion")
        break
print(num)
print("cuarto bucle terminado \n")

 #ciclo infinoto + break 

while True: 
    parametro= input ("<")
    if parametro == "exit" : 
        break 
    else: 
        print (parametro)

#imprimiendo una lista de forma vertical no esta bien hecho 
'''for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)'''

newlista= [1,2,3,4,5,6,7,8,9,10] #i,j, aux, recorre toda la lista elemento por elemento
for i in newlista:
    print(i)

for i in range (1,11):     # declaro la lista del del 1 al 11 un rango, imprime del 1 al 10 
    print (i)

for i in range (1,3):  #2 o mas elementos
    print(i)
    



