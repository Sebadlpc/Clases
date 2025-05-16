sw = 1
puntos= 100000
while sw==1:
    print("1. Ver mis puntos")
    print("2. Gastar mis puntos")
    print("3. Salir")
    op=(int(input("Seleccione una opcion: ")))
    if op==1:
        print(f"Sus puntos son {puntos}")
    if op==2:
        print("Seleccione el producto a canjear ")
        print("1.- Gift Cars de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de 25.000 puntos")
        print("3.- Disco duro portatil, valor de 30.000 puntos")
        continu=int(input("Seleccione la opcion: "))
        if continu==1:
            puntos-=10000
            print(f"Canje exitoso, le quedan {puntos} puntos")
        elif continu==2:
            puntos-=25000
            print(f"Canje exitoso, le quedan {puntos} puntos")
        elif continu==3:
            puntos-=30000
            print(f"Canje exitoso, le quedan {puntos} puntos")
    if op==3:
        sw=0 ##Tambien se puede usar un exit() o break
---------------------------------------------------------------------------
sw=1
while sw==1:
    print("Opciones a elegir: \n"
          "1. Ver mi saldo \n"
          "2. Retirar dinero \n"
          "3. Salir")
    opcion=int(input("Seleccione una opcion: "))
    try:
        if(opcion >0 and opcion <4):
            if opcion == 1:
                print(f"Tienes un saldo de $500000")
                op=int(input("Presione (1) para volver atras o (2) para salir: "))
                if op==1:
                   sw=1
                elif op==2:
                   print("Cierre de sesión exitoso, adiós")
                   sw=0
            elif opcion==2:
                print("Transferencia relizada")
                op=int(input("Presione (1) para volver atras o (2) para salir: "))
                if op==1:
                   sw=1
                elif op==2:
                   print("Cierre de sesión exitoso, adiós")
                   sw=0
            elif opcion==3:
                print("Cierre de sesión exitoso, adiós")
                sw=0
            else:
                print("Opcion fuera de rango")
    except:
        print("Ingreso erroneo")
--------------------------------------------------------------------------------------------
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
