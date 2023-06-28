num=2 
vacio=[]
while (num <= 29): 
    num += 3 
    vacio.append(num)
    print(num)

print(vacio)
vacio.pop()
print(vacio)

a= vacio[0] 
b= vacio[5]

print(a+b)

c= vacio[2]
d=vacio[4]
e= vacio [6]
f=vacio [8]

print(a+c+d+e+f)