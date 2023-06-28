nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")


prim_nombre1 = nombre1[0]
prim_nombre2 = nombre2[0]

# Obtener la última letra de cada nombre
ult_nombre1 = nombre1[-1]
ult_nombre2 = nombre2[-1]

# Comparar las letras iniciales y finales
if prim_nombre1 == prim_nombre2:
    print("Ambos nombres comienzan con la misma letra.")
elif ult_nombre1 == ult_nombre2:
    print("Ambos nombres terminan con la misma letra.")
else:
    print("Los nombres difieren tanto en la letra inicial como en la final.")
