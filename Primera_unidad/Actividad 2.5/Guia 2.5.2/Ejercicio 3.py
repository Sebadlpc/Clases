sw=1
saldo=0
while sw==1:
    print("Opciones a elegir: \n"
          "1. Ver mi saldo \n"
          "2. Cargar saldo \n"
          "3. Salir")
    opcion=int(input("Seleccione una opcion: "))
    try:
        if(opcion > 0 and opcion < 4):
            if opcion == 1:
                print(f"Tiene un saldo de {saldo}")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu ==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            elif opcion == 2:
                print("¿Cuánto desea cargar? \n"
                      "1.- $1.000 \n"
                      "2.- $5.000 \n"
                      "3.- $20.000")
                continu = int(input("Seleccione la opción: "))
                if continu ==1:
                    saldo = saldo+1000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                elif continu ==2:
                    saldo = saldo+5000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                elif continu ==3:
                    saldo = saldo+20000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
            if opcion == 3:
                print("Muchas gracias por ocupar el servicio, adiós")
                sw=0
            else:
                print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")