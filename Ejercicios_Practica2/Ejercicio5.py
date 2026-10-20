saldo = 1000

opcion = 0

while saldo>0 and opcion!=1:
    print("Quieres retirar dinero o salir?")
    opcion = int(input("1 Para Salir || 2 Para retirar : "))
    if opcion == 2:
        cantidad = int(input("Introduce la cantidad a retirar: "))
        while cantidad>saldo:
            print("La cantidad a retirar es mayor al saldo que posees. ERROR.")
            cantidad = int(input("Introduce de nuevo la cantidad: "))
        saldo=saldo-cantidad
        print("Saldo actual:",saldo)
    elif opcion == 1:
        print("Saliendo . . .")
    else:
        print("Opción no válida.")