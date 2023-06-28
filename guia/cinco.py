
lab1 = int(input("Ingrese la nota del Lab 1: "))
lab2 = int(input("Ingrese la nota del Lab 2: "))
lab3 = int(input("Ingrese la nota del Lab 3: "))

promedio = lab1 * 0.3 + lab2 * 0.4 + lab3 * 0.3
print(promedio)


if promedio < 40.0:
    print("El estudiante reprobó la asignatura.")
elif promedio>= 40.0 and promedio < 60.0:
    print("El estudiante aprobó la asignatura.")
else:
    print("El estudiante aprobó la asignatura con distinción.")
