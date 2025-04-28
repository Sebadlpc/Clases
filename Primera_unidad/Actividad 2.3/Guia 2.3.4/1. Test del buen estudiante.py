titulo= "Bienvenido al 'Test del buen estudiante'"
print("\n" + titulo + "\n"+"-" * len(titulo)+ "\n")
print("Responda con una 's' si es si o con una 'n' si es no.")

puntuacion=0

opcion= input("¿Deja para despues lo que puede hacer ahora?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿Prestas atencion en clases?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿Resuelve sus dudas con el profesor?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿Prueba sus hipótesis antes de preguntar?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿utiliza su tiempo libre para aprender ocsas nuevas?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()
    
opcion= input("¿Utiliza otra fuente de informacion para resolver dudas?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿Estudia solo un dia antes de la prueba?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿A sus amigos solo les gusta pasar el rato?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿A menudo realiza acciones que no son importantes?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿Le gustaria no tener que trabajar?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿Le gusta leer?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

opcion= input("¿le gustan las redes sociales?")

if opcion == "s":
    puntuacion += 1
elif opcion == "n":
    puntuacion += 0
else:
    print("Las opciones eran s o n.")
    exit()

if puntuacion < 4:
    print("Usted es un alumno de buen desempeño")
elif puntuacion >= 4 and puntuacion < 7:
    print("Usted es un alumno que puede mejorar")
elif puntuacion >=7 and puntuacion < 10:
    print("Usted es un alumno con algunos desafios")
elif puntuacion >= 10:
    print("Usted alumno con muchos desafios")

