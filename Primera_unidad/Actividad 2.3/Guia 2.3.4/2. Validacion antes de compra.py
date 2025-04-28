print("Ingrese todos los datos antes de realizar la compra")
print("Todos los datos son obligatorios")

nombre=input("Ingrese su nombre: ")
telefono=input("ingrese su telefono: ")

print("Ingrese producto y cantidad")
producto=input("Ingrese nombre del producto: ")
cantidad=int(input("Ingrese la cantidad del producto: "))

print("Esta seguro que quieres pagar")
respuesta=input("'S' o 'N'")


if respuesta == "S":
  if nombre =="" or telefono =="" or producto == "" or cantidad <= 0:
    print("Faltan datos por ingresar")
    print(f"Nombre: {nombre}")
    print(f"Telefono: {telefono}")
    print(f"Producto: {producto}")
    print(f"Cantidad: {cantidad}")

  else:
    print("Su compra se ha realizado con exito, vuelva pronto")

else:
    print("No se ha realizado la compra")
