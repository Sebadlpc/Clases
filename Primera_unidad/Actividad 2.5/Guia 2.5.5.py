sw=1
usuario1=None
usuario2=None
usuario3=None
contrasena1=None
contrasena2=None
contrasena3=None
while sw==1:
    print("Sus opciones son: \n"
            "1) Iniciar sesion \n"
            "2) Registrar usuario \n"
            "3) Salir")
    opcion = int(input("Ingrese una opcion: "))
    if (opcion>0 and opcion<4):
        if opcion == 1:
            if not usuario1 and not usuario2 and not usuario3:
                print("Debes registrar un usuario antes")
                sw=1
            else:
                usuario_ingresado=input("Ingrese el usuario: ")
                contrasena_ingresada=input("Ingrese la contraseña: ")
                if (usuario_ingresado==usuario1 and contrasena_ingresada==contrasena1) or \
                    (usuario_ingresado==usuario2 and contrasena_ingresada==contrasena2) or \
                    (usuario_ingresado==usuario3 and contrasena_ingresada==contrasena3):
                    print("Bienvenido")
                else:
                    print("Usuario o contraseña incorrectos")
            
                              
                
            
        
        elif opcion == 3:
            sw=0
        
         
        
        

