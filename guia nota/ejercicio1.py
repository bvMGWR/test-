a= 'la Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica.'
print(a)
print(type(a))
b= a.lower()
c= b.split()
contador= 0
vacio=[]
for uni in c : 
    if uni == "universidad": 
        contador = contador+1
        vacio.append(uni)

print ("la palabra universidad se repite ",contador , "veces")
vacio= tuple(vacio)
print(vacio)




