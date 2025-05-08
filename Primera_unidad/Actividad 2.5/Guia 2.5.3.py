sw=1
cuenta=-100000
valorcompra=0
while sw==1:
    print("Opciones a elegir: \n"
          "1. Pago de tarjeta de credito \n"
          "2. Simulacion de compras \n"
          "3. Salir")
    opcion = int(input("Ingrese la opcion que deseas: "))
    try:
        if(opcion>0 and opcion<4):
            if opcion ==1:
                print(f"Tu deuda es de ${cuenta}")
                pago=int(input("Cuanto deseas pagar: "))
                if pago>=0:
                    cuenta+=pago
                    print(f"Tu deuda ahora es de ${cuenta}")
                else:
                    print("Accion erronea")
                    sw=1

            elif opcion==2:
                compras=int(input("Cuantas compras quieres hacer?: "))
                for i in range(compras):
                    cobro=int(input(f"Ingrese el valor de la compra {i+1}: "))
                    cuenta -= cobro
                    print(f"Tu deuda es de ${cuenta}")

            elif opcion==3:
                print("Cierre de sesión exitoso, adiós")
                sw=0
    except:
        print("Ingreso erroneo")
