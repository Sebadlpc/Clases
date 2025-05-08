precio=input("Dame el precio del producto con '$': ")
if precio.startswith('$'):
    precio=precio[1:]
    if precio.isdigit():
       if len(precio)>=3:
        print("Este precio es valido")
       else:
          print("Este precio no es valido")
    else:
       print("Este precio no es valido")

else:
    print("Falta el $")
precio=float(precio)
codigo=input("Tiene algun codigo?: ")
if 'DESC' in codigo:
   precio_final=float(precio*0.9)
   print(f"El precio final es ${precio_final}")
elif codigo.endswith('VIP'):
   precio_final=float(precio*0.85)
   print(f"El precio final es ${precio_final}")
else:
   print(f"El precio final es ${precio}")