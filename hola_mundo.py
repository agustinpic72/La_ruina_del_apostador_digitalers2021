import random
lista=[0,1]
resultado=random.choices(lista,weights=[0.2,0.8])
resultadovich=resultado.pop(0)
fichas=50
tmp=0
while fichas>0:
    resultado=random.choices(lista,weights=[0.4,0.6])
    resultadovich=resultado.pop(0)
    if resultadovich==1:
        fichas-=1
        tmp+=1
    elif resultadovich==0:
        fichas+=1
        tmp+=1
    if fichas==0:
        print("perdiste moster")
    
    

        