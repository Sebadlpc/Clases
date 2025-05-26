mayor=None
menor=None
while True:
    op=(int(input("1. Ingresar numeros \n"
                  "2. Mostrar mayor \n"
                  "3. Mostar menor \n"
                  "4. Salir \n"
                  "Ingrese una opcion: ")))
    
    if op==1:
        cant=int(input("Cuantos numeros quieres ingresar: "))
        try:
            for i in range(cant):
                num=int(input("Ingrese un numero entre el 0 y el 100: "))
                if 0 <= num <=100:
                    print("Ingrese exitoso")
                    if mayor is None or num > mayor:
                        mayor=num
                    if menor is None or num < menor:
                        menor=num
                    
                else:
                    print("Debe ingresar un numero entre el 0 y el 100")
        except ValueError:
            print("Debe ser un numero entero")

    elif op==2:
        if mayor is None:
            print("Aun no se han ingresado numeros")
        else:
            print(f"El numero mayor es {mayor}")
       
    
    elif op==3:
        if menor is None:
            print("Aun no se han ingresado numeros")
        else:
            print(f"El numero menor es {menor}")
        

    elif op==4:
        print("Hasta luego")
        break
    
    else:
        print("Debe ingresar una opcion valida")