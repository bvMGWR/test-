a= int(input ("escribe un numero"))
if (a)% 2 == 0 :
    print("el numero es par")
else: 
    print("el numero es inpar")

primo = True
if a < 2:
    primo = False
else:
    for i in range(2, a):
        if a % i == 0:
            primo = False
            break

if a:
    print("El número es primo.")
else:
    print("El número no es primo.")

if a >= 50:
    print("El número es igual o mayor a 50.")
else:
    print("El número es menor a 50.")
