cuidades= ["santigo", "temuco", "osorno", "punta arenas"]
calidad_aire= [134,99,245,50]

print ( "cuidad con el indice calidad de aire mas alto ",cuidades [3], calidad_aire[3])
print ( "cuidad con el indice calidad de aire mas bajo ",cuidades [2], calidad_aire[2])
dato_1= tuple(zip(cuidades,calidad_aire))

print(min(dato_1))
print (max(dato_1))
    