num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
contador = 0
if num2<num1:
    temporal = num2
    num2 = num1
    num1 = temporal

for i in range (num1+1,num2):
    if i%2==0:
        print(i)
        contador +=1

print("Total de numeros pares:",contador)