import random
opciones= ["Me quiere mucho","Me quiere poquito","Me quiere nada"]
num_hojas= random.randint(5,15)
for _ in range(num_hojas):
    print(opciones[random.randint(0,2)])
if opciones[random.randint(0,2)] == "Me quiere mucho":
    print("\nFelicidades, ¡!Te quieren Mucho!!!\n"+ "Mucho!!!\n" * 3)
else:
    print("\nLo siento, no te quieren mucho esta vez.")  