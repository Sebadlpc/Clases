esprimo = 0
noesprimo = 0

try:
    cantidad = int(input("Ingrese el total de números a confirmar: "))
except ValueError:
    print("Error, el valor ingresado no es un número entero")
    exit() 

for _ in range(cantidad):  
    nums = int(input("Ingrese un número a verificar: "))
    primo = True
    
    if nums < 2:
        primo = False
    else:
        for i in range(2, int(nums ** 0.5) + 1):  
            if nums % i == 0:
                primo = False
                break 
    if primo:
        print(f"{nums} es primo")
        esprimo += 1
    else:
        print(f"{nums} no es primo")
        noesprimo += 1

print(f"\nTotal de números primos: {esprimo}")
print(f"Total de números no primos: {noesprimo}")