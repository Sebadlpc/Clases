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