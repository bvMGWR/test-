a= input ("ingrese el primer numero")
print (a)
b= input ("ingrese el segundo numero")
print (b)
c= input ("ingrese el tercer numero")
print (c)
if a > b and a > c:
    print (a,"es el numero mayor")
else: 
    if b > a and b > c:
        print(b, "es el numero mayor")
    else: 
        if c> a and c> b: 
            print ( c, "es el numero mayor")
if a < b and a < c:
    print (a,"es el numero menor")
else: 
    if b < a and b < c:
        print(b, "es el numero menor")
    else: 
        if c< a and c< b: 
            print ( c, "es el numero menor")
