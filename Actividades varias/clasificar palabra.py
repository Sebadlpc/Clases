##Este programa sirve para clasificar palabras
Palabra=input("Ingrese su palabra: ")
if len(Palabra)>=1 and len(Palabra)<=5:
    print("La palabra es corta")
elif len(Palabra) >=5 and len(Palabra)<=8:
    print("La palabra es media")
elif len(Palabra) >=8:
    print("La palabra es larga")
elif len(Palabra) == 0:
    print("La palabra es vacia")
