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

if calidad_aire[3] >=0 or calidad_aire[3] < 50 :
    print("ICA buena")
else: 
    if calidad_aire[3] > 51 or calidad_aire[3] < 100: 
        print("ICA moderada")
    else: 
        if calidad_aire[3] > 101 and calidad_aire[3] < 150:
            print("ICA dañina para gurpos sensibles")
        else: 
             if calidad_aire[3] > 151 and calidad_aire[3] < 200:
                 print("ICA dañina a la salud")
             else :
                 if calidad_aire[3] > 201 and calidad_aire[3] < 300:
                     print("ICA muy dañina a la salud")
                 else: 
                     if calidad_aire[3] > 300:
                         print("ICA peligrosa")
                         