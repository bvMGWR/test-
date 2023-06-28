
nombre= input ("¿cual es tu nombre")
asignatura=input ("¿cual es tu asignatura?")
laboratorio1 = float(input ("¿cual es la nota1?"))
laboratorio2 = float(input ("¿cual es la nota2?"))


print (type ("nota laboratorio1"))
print (type ("nota laboratorio2"))


nota_final= int(laboratorio1 ) * 0.3 + int(laboratorio2) * 0.7
print (nota_final)
dic= {
    "nombre del estudiante" : nombre,
    "nombre de la asignatura" : asignatura,
    "nota laboratorio1" : laboratorio1,
    "nota laboratorio2" : laboratorio2,
    "nota final" : round (nota_final, 1)

}



