edad = int(input("Ingrese su edad: "))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("--------------------------")

ValidacionUser= input("Ingrese usuario: ")
ValidacionPws= input("Ingrese su contraseña: ")
user1= "pedro"
pws1= "1234"
user2= "angel"
pws2= "a4s1"

if ValidacionUser == user1 and ValidacionPws == pws1 or ValidacionUser == user2 and ValidacionPws == pws2:
    print("Acceso autorizado")
else:
    print("User o password incorecta")

print("---------------------------")

nota1=float(input("Ingrese nota: "))
nota2=float(input("Ingrese nota: "))
nota3=float(input("Ingrese nota: "))

Promedio=float((nota1+nota2+nota3)/3)
print(f"Su promedio fue un {Promedio}")
if Promedio >= 4:
    print("Aprobado")
else:
    print("Reprobado")

print("--------------------------")
titulo= "Bienvenidos a este quiz de animeles acuaticos"
print("\n" + titulo + "\n"+"-" * len(titulo)+ "\n")

puntuacion= 0

opcion= input("Pregunta 1: ¿Cual de los siguientes animales vive en el agua? \n"
              "A) Perro\n"
              "B) Cocodrilo\n"
              "C) Conejo\n"
              "D) Tiburon\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 0,5
elif opcion == "C":
    puntuacion += 0
elif opcion == "D":
    puntuacion += 1
else:
    print("Las opciones eras A, B, C o D.")
    exit()

print("--------------------------")


titulo= "Bienvenidos a este quiz de cuan fan eres de castillo (Un amigo)"
print("\n" + titulo + "\n"+"-" * len(titulo)+ "\n")

puntuacion= 0

opcion= input("Pregunta 1: ¿Cuantos años tiene? \n"
              "A) 17 Años\n"
              "B) 20 Años\n"
              "C) 23 Años\n"
              "D) 8 Años\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 0
elif opcion == "D":
    puntuacion += 0
else:
    print("Las opciones eras A, B, C o D.")
    exit()
              
opcion= input("Pregunta 2: ¿Cuantas mascotas tiene? \n"
              "A) 2\n"
              "B) 3\n"
              "C) 1\n"
              "D) ninguna\n")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 0
elif opcion == "C":
    puntuacion += 5
elif opcion == "D":
    puntuacion += 0
else:
    print("Las opciones eras A, B, C o D.")
    exit()

opcion= input("Pregunta 3: ¿Como no le gustaria que lo recordaran? \n"
              "A) El Youtuber frustrado\n"
              "B) Benjita\n"
              "C) Centauro amoroso\n"
              "D) Blaster\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 0
elif opcion == "D":
    puntuacion += 0
else:
    print("Las opciones eras A, B, C o D.")
    exit()


if puntuacion >= 15:
    print("Eres un verdadero fan")
elif puntuacion >= 10:
    print("Lo conociste moderadamente")
elif puntuacion >= 5:
    print("No lo hubiese conocido")
