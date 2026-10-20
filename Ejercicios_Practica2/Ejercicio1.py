segundos = int(input("Hola! Introduce los segundos que deseas convertir: "))
minutos = 0
horas = 0

if segundos>=60:
    minutos = int(segundos/60)
    segundos = segundos%60
    if minutos>=60:
        horas = int(minutos/60)
        minutos = minutos%60

print("Segundos:",segundos,",Minutos",minutos,"y horas",horas)



