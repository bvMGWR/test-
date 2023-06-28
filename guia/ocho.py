
mes = input("Ingrese un mes: ")


estaciones = {
    'enero': 'verano',
    'febrero': 'verano',
    'marzo': 'verano',
    'abril': 'otoño',
    'mayo': 'otoño',
    'junio': 'invierno',
    'julio': 'invierno',
    'agosto': 'invierno',
    'septiembre': 'primavera',
    'octubre': 'primavera',
    'noviembre': 'primavera',
    'diciembre': 'verano'
}

a = estaciones.get(mes)

print(f"La estación correspondiente al mes de {mes} es {a}")


