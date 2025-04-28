print("Bienvenidos a Cesars Pizza")
print("Nuestra seleccion de pizzas son las siguientes")
print("1. Pepperoni \n"
      "2. Queso \n"
      "3. Jamon \n"
      "4. 4in1 \n"
      "5. Hula Hawaiian \n"
      "6. Ultimate supreme \n" 
      "7. Veggie \n" 
      "8. 3 Meat treat \n" 
      "9. Super cheese 4in1 \n" 
      "10 Chicken BBQ") 
opcion=input("Eliga su pizza. Ponga el numero de la pizza: ")
cantidad=int(input("¿Cuantas pizzas desea?: "))

if opcion == "1":
    precio = 6000
elif opcion == "2":
    precio = 7000
elif opcion == "3":
    precio = 8000
elif opcion == "4" or opcion == "5":
    precio = 10000
elif opcion == "6":
    precio = 11000
elif opcion in ["7", "8", "9", "10"]:
    precio = 12000
    
neto=precio*cantidad
iva=float(neto*0.19) 
total=neto+iva

print(f"Neto: {neto}")
print(f"IVA: {iva}")
print(f"Total: {total}")