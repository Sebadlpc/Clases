while True:
    print("Tus opciones son: \n"
        "1. Sumar \n"
        "2. Multiplicar \n"
        "3. Dividir \n"
        "4. Salir")
    op = int(input("¿Qué opción deseas?: "))
    if op==1:
        lista_suma=[]
        numsum=int(input("Que numero desea sumar?: "))
        cantidadsuma=int(input("Cantidad de numeros a sumar?:"))
        for i in range(cantidadsuma):
            lista_suma.append(int(input(f"Ingrese el numero {i+1}: ")))
            nueva_lista=[num+numsum for num in lista_suma]
        print(f"Sus numeros son: {lista_suma}")
        print(f"El resultado de la suma es: {nueva_lista}")
        break
        
    if op==2:
        lista_mult=[]
        nummult=int(input("Que numero desea multiplicar?: "))
        cantidadmult=int(input("Cantidad de numeros a multiplicar?:"))
        for i in range(cantidadmult):
            lista_mult.append(int(input(f"Ingrese el numero {i+1}: ")))
            nueva_lista2=[num*nummult for num in lista_mult]
        print(f"Sus numeros son: {lista_mult}")
        print(f"El resultado de la multiplicacion es: {nueva_lista2}")
        break

    if op==3:
        lista_div=[]
        numdiv=int(input("Que numero desea dividir?: "))
        cantidaddiv=int(input("Cantidad de numeros a dividir?:"))
        for i in range(cantidaddiv):
            lista_div.append(int(input(f"Ingrese el numero {i+1}: ")))
            nueva_lista3=[num/numdiv for num in lista_div]
        print(f"Sus numeros son: {lista_div}")
        print(f"El resultado de la divicion es: {nueva_lista3}")
        break
    
    if op==4:
        print("Hasta luego")
        break
       
    else:
        print("Opción no válida, por favor intenta de nuevo")
        