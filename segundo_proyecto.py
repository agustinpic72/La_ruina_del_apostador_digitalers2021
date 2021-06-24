import random
import time

inicio=time.time()



print("**************************")
print("Bienvenido a casino Royale")
print("**************************")

#Funcion
def apuestas(fichas,probabilidad,maximo_jugado):
    tmp=0
    while fichas>0 and tmp<maximo_jugado:
        lista=[0,1]
        resultado= random.choices(lista,weights=[1-probabilidad,probabilidad])
        borrame=resultado.pop(0)
        if borrame==1:
            fichas+=1
            #print("Ganaste")
        elif borrame==0:
            fichas-=1
            #print("Perdiste")
        tmp+=1
    if fichas == 0:
        return(f"perdiste, te quedan {fichas} fichas y apostaste {tmp} veces")
    if fichas >0:
        return(f"ganaste, te quedan {fichas} fichas y apostaste {tmp} veces")


#Llamar 20 veces la funcion
for _ in range(1,21):
    print(f"\nResultado de la noche numero {_}:")
    print(apuestas(50 , 0.4 , 300))#fichas, probabilidad, maximo jugado
    
    
    
    
#Tiempo empleado en correr el programa
fin=time.time()
diferencia=fin-inicio
print(f"\nDemoramos {diferencia} en correr todo el programa")

