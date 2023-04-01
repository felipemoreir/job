string = input("digite a string que deseja inverter:")
contador=-1
aux=0

for i in string:
    contador+=1

print("a frase invertida fica:")

for i in range(contador,-1,-1):
    print(string[i],end="")
    

