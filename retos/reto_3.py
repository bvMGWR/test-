cuidades= ["santigo", "temuco", "osorno", "punta arenas"]
calidad_aire= [134,99,245,50]
min=min(calidad_aire)
max= max(calidad_aire)
print(min)
print(max)
nueva= cuidades[calidad_aire.index(min)]
nuevo= cuidades[calidad_aire.index(max)]


print ( "cuidad con el indice calidad de aire mas alto ",nueva)
print ( "cuidad con el indice calidad de aire mas bajo ",nuevo)
dato_1= list(zip(cuidades,calidad_aire))
print (dato_1)

print("punta arenas tiene:")

if nueva >=0 or nueva < 50 :
    print("ICA buena")
else: 
    if nueva > 51 or nueva < 100: 
        print("ICA moderada")
    else: 
        if nueva > 101 and nueva < 150:
            print("ICA dañina para gurpos sensibles")
        else: 
             if nueva > 151 and nueva < 200:
                 print("ICA dañina a la salud")
             else :
                 if nueva > 201 and nueva < 300:
                     print("ICA muy dañina a la salud")
                 else: 
                     if nueva > 300:
                         print("ICA peligrosa")


print("santiago tiene:")


if nuevo >=0 or nuevo < 50 :
    print("ICA buena")
else: 
    if nuevo > 51 or nuevo < 100: 
        print("ICA moderada")
    else: 
        if nuevo > 101 and nuevo < 150:
            print("ICA dañina para gurpos sensibles")
        else: 
             if nuevo > 151 and nuevo < 200:
                 print("ICA dañina a la salud")
             else :
                 if nuevo > 201 and nuevo < 300:
                     print("ICA muy dañina a la salud")
                 else: 
                     if nuevo > 300:
                         print("ICA peligrosa")                            
                         