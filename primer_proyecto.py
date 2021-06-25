####Primer version####
import random
import time

inicio=time.time()

print("**************************")
print("Bienvenido a casino Royale")
print("**************************")

#fichas = int(input("\nFichas: "))
fichas=50
probabilidad = 0.4
#maximo_jugado = int(input("\nNumero maximo de tiradas: "))
maximo_jugado=300
tmp=0
contador=0
ganaste=0
perdiste=0

for _ in range(0,20):
    fichas=50
    tmp=0
    while fichas>0 and tmp<maximo_jugado:
        lista=[0,1]
        resultado=random.choices(lista,weights=[probabilidad,0.6])
        borrame=resultado.pop(0)
        if borrame==0:
            fichas+=1
            #print("Ganaste")
        elif borrame==1:
            fichas-=1
            #print("Perdiste")
        tmp+=1
        
        if fichas==0:
            #print("perdiste we")
            contador+=tmp
            perdiste+=1
            
    if fichas>0:
        contador+=tmp
        ganaste+=1
      
        
        
print("Jugaste un promedio de: ",str(contador/20),"veces")
print("Ganaste: ",str(ganaste),"\nPerdiste: ",str(perdiste))
fin=time.time()
diferencia=fin-inicio
print("Demoramos: ",str(diferencia))
    
    
    
    

