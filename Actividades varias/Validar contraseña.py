print("Necesitamos validar tu contraseña\n"
                         "(Tiene que tener: \n"
                         "-Al menos 8 caracteres \n" 
                         "-Al menos un numero \n" 
                         "-Al menos una mayuscula)")
contraseña=input("Porfavor ingrese su contraseña: ")
if len(contraseña) >=8 and any (char.isdigit() for char in contraseña) and any(char.isupper() for char in contraseña):
    print("La contraseña es valida")
else:
    print("La contraseña no cumple con los requisitos")
