import os
from re import A, X
os.system("cls")

num = int(input("Cuantos numeros se desean agregar:"))

a = []
b = []
for i in range(1,num+1):
    n = int(input("Ingrese numero {}: ".format(i)))
    if n >= 1 and n <= 99:
        if n%2 == 0:
            a.append(n)
        else:
            b.append(n)

    else:
        print("Eror, el numero no esta dentro del rango")
        break

print("Hay {} numeros pares".format(len(a)))
print("Hay {} numeros impares".format(len(b)))