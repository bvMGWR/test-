


licencia= False
edad= 19 
automovil= False
if licencia== True: #no dice que la licencia es verdadera, se esta comparando con true por eso imprimie el else 
    print( "puedo conducir porque tengo licencia")
else: 
    print ("no tengo licencia para conducir")
    licencia = False
edad = 19
automovil = False

#¿Estará correcto este código?                                                      
"""if licencia == True:
    print('Puedo conducir porque tengo licencia')
#¿Estará correcto este código?                                                  
print(Testeando los comparadores y el IF')
if licencia:
    print( 'Puedo conducir porque tengo licencia')
else:
    print('No tengo licencia para conducir')"""



print('No tengo licencia para conducir')


#Sucede que la variable licencia se esta comparando con True,
#y se debe asignar directamente, es decir no se ocupa el ==, sino solamente el igual (=)



print("Utilizando el segundo condicional IF")

if edad:
    print('Puedo conducir porque soy mayor de edad\n')    
else:
    print('No puedo conducir soy menor de edad\n')
    


print( 'Utilizando el tercer condicional IF')
if edad >= 18:
    print('Puedo conducir porque soy mayor de edad\n')
    
else:
    print('No puedo conducir soy menor de edad\n')
   


print(' 02 UTILIZANDO IF y ELIF, ELSE ')

if licencia and edad >= 18:
    print('Puedo conducir porque soy mayor de edad y tengo licencia')
    
elif automovil:
    print('Tengo automovil, pero no tengo licencia ni la edad necesaria')
else: 
    print('No puedo conducir no tengo ni la edad, ni licencia ni automovil')

