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