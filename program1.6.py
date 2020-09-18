while True: 
    print("Opción 1 - Comenzar el programa")
    print("Opción 2 - Imprimir listado")
    print("Opción 3 - Finalizar programa")
    opcion=int(input("Opción elegida:"))
    if opcion==1:
        print("Comenzamos")
    elif opcion==2:
        print("Listado:")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta pronto")
        break
    else: 
        print("Opción incorrecta. Debe ser 1, 2 o 3")
        

