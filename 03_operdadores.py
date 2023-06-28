##operadores
a= 2
b=6 
suma= a +b 
resta= a-b
multi= a*b 
div= a/b 
mod= a%b #modulo 
ex= a**b #exponente
co= a//b #cocciente 

###de comparacion 
igual= a==b 
dis= a!=b 
may= a>b 
men= a<b 
mayig= a>=b 
menig= a<=b 

####

#cambian
bencina = True
encendido = True
encendido = False
edad = 19

# AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

# OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

# NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

# NOT junto al OR
if not bencina or encendido:
    print("Utilizando NOT Y OR:  El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

# NOT junto al AND y OR
if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")