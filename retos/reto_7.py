

def frase_(frase):
    a= (frase.split()) #funcion que separa 
    frases= {
        a[0]: a[1:], 
    }
    print(frases)
    frase.replace(" ", "")
    print(len((frase.replace(" ", ""))))

frase= input("ingrese una frase \n")
print(frase_(frase))