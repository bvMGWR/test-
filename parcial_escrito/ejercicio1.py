pacientes = [["pedro", 1.78], ["constanza", 1.56], ["amanda", 1.62], ["dario", 1.89], ["fernanda", 1.67]]




def insertar_paciente(pacientes, nuevo_paciente):
    pacientes.append(nuevo_paciente)



def buscar_paciente(pacientes, nombre_paciente):
    for paciente in pacientes:
        if paciente[0] == nombre_paciente:
            return paciente
    return None

print("La estatura menor entre todos los pacientes: ", )

insertar_paciente(pacientes,["ricardo", 1.71])

print("Lista de pacientes actualizada: ", pacientes)

a= buscar_paciente(pacientes,"dario")
if a:
    print("Paciente encontrado:", a[0],a[1])
else:
    print("No se encontró el paciente.")