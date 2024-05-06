import random
print("Bienvenido al juego de calfun´s planet")
#Esto es para que el usuario elija el numero de vueltas dadas por el juego
numdevueltas=int(input("Ingrese cuantas vueltas quiere que el juego haga="))
#Esta variable es para el juego ande las veces que el usuario indico
vueltasdadas=0
while vueltasdadas<numdevueltas:
 #numero aleatorio para las 3 opciones posibles
 numal=random.randint(1,3)
 if numal==1:
  print("No me quiere")
 elif numal==2:
  print("Me quiere mucho")
 else:
  print("Me quiere poquito")  
 vueltasdadas=vueltasdadas+1
#Para mostrar cual opcion quedo al final
if numal==1:
 print("!!!!FELICIDADES NO TE QUIEREN!!!!")
elif numal==2:
 print("!!!FELICIDADES TE QUIEREN MUCHO!!!!")
else:
 print("!!!!FELICIDADES TE QUIEREN POQUITO!!!") 
print("GRACIAS POR JUGAR")
