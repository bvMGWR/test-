set1= {100,250,300,1000}
set2= {150, 250, 500, 1000}

for i in set1: 
   if i==100: 
      print("el valor 100 esta en el set1")

print("\n")

for i in set2: 
   if i==100: 
      print("el valor 100 esta en el set2")
   else: 
      print("el valor 100 no esta en el set2")

print("\n")

for i in set1: 
   if i==500 : 
      print("el valor 500 esta en el set1")
   else:
      print("el valor 500 no esta en el set1")

print("\n")


for i in set1: 
   if i==700 : 
      print("el valor 700 esta en el set1")
   else:
      print("el valor 700 no esta en el set1")


print("\n")
for i in set2: 
   if i==500 : 
      print("el valor 500 esta en el set2")
   else:
      print("el valor 500 no esta en el set2")

print("\n")

for i in set2: 
   if i==700 : 
      print("el valor 700 esta en el set2")
   else:
      print("el valor 700 no esta en el set2")

print("\n")


a=list(set1)
b=list(set2)

c= a+b

print(c)

unido= set(c)
print(unido)

print(a.count(100))
print(a.count(500))
print(b.count(500))
print(a.count(700))
print(b.count(700))
