titulo= "La gran aventura"
print("\n" + titulo + "\n"+"-" * len(titulo)+ "\n")
print("Puedes moverte a la derecha con 'd', a la izquierda con 'a' o hacia adelante con la 'w'")

print("Inicia la aventura")
opcion=input("Corres hacia la montaña nevada. Un ruido te detiene. (Muevete hacia algun lado): ")
if opcion == "a":
    print("Ves como un oso se acerca hacia ti.")
    opcion= input("Te quedas quedas quieto. Despues de un tiempo te comienzas a deslizar hacia un lado: ")
    if opcion == "w":
        print("Te mueves un poco hacia delante y el oso te mata.")
    elif opcion == "a":
        print("Una planta carnivora te come.")
    else:
        print("Te mueves un poco a la derecha y ves un tunel que te lleva al siguiente nivel.")
elif opcion =="d":
    print("Ves una serpiente que esta a 30 cm de tu pie.")
    opcion= input("Te quedas muy quieto. Despues de un momento te comienzas a deslizar hacia un lado.")
    if opcion == "w":
        print("Si avanzas un poco la serpiente te muerde y mueres con dolor.")
    elif opcion == "a":
        print("te mueves hacia la izquiera y una planta carnivora te come.")
    else:
        print("Te mueves un poco a la derecha y ves un tunel que te lleva al siguiente nivel.")
else:
    print("Ves una luz que se acerca a ti")
    opcion= input("Te quedas muy quieto. Despues de un momento te comienzas a deslizar hacia un lado.")
    if opcion == "w":
        print("El tunel te lleva al siguiente nivel")
    elif opcion== "a":
        print("Te mueves a la izquierda y una planta carnivora te come.")
    else:
        print("Te mueves un poco a la derecha y un leon se abalnza contra ti y te come.")
print("Fin de la partida. Muchas gracias por jugar.")