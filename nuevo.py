if calidad_aire[3] >=0 and calidad_aire[3] < 50 :
    print("ICA buena")
else: 
    if calidad_aire[3] > 51 and calidad_aire[3] < 100: 
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