a= input ( " ingrese el lado1 del triangulo ")
b= input ("ingrese el lado2 del triangulo ")
c= input ("ingrese el lado3 del tirangulo ") 
if a==b and a==c: 
        print("el triangulo es equilatero")
else: 
    if a==b and a!=c: 
        print("el triangulo es isoceles ")
    else: 
         if a!=b and a!=c: 
              print ("el triangulo es escaleno")

#type usar para saber a que tipo de dato corresponde 
#int para trasformar o declarar la variables como entero 
p= ( (int(a)+int(b)+int(c))/2)
print (p)
area= p*(p-(int(a)))*(p-(int(b)))*(p-(int(c)))
print (area)
