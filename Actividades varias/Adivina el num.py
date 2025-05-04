import random
titulo="Bienvenidos a Adivina el numero"
print("\n" + titulo + "\n"+"-" * len(titulo)+ "\n")

print("Para empezar ingrese dos numeros enteros que representan el rango numérico \n"
      "(El primer numero debe ser menor que el segundo)")
n1=int(input("Ingrese el limite inferior: "))
n2=int(input("Ingrese el limite superior: "))
numero = random.randint(n1, n2)
ajuste=(numero/4)*4

primer_intento=int(input("Intente adivinar el numero: "))
if primer_intento == ajuste:
    print("Felicitaciones, acertaste a la primera")
    exit()
elif primer_intento != ajuste:
    if primer_intento > ajuste:
        print("El numero es menor")
    elif primer_intento < ajuste:
        print("El numero es mayor")
        
segundo_intento=int(input("Intente adivinar el numero: "))
if segundo_intento == ajuste:
    print("Felicidades, acertaste el numero")
    exit()
elif segundo_intento != ajuste:
    if segundo_intento > ajuste:
        print("El numero es menor")
    elif segundo_intento < ajuste:
        print("El numero es mayor")
        
tercer_intento=int(input("Intente adivinar el numero: "))
if tercer_intento == ajuste:
    print("Felicidades, acertaste el numero")
else:
    print(f"Perdiste, el numero era {ajuste}") 