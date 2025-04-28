livianos = 0
normales = 0
total_a_pagar = 0

try:
    cantidadbultos = int(input("Cuántos bultos desea registrar: "))
    if cantidadbultos <= 0:
        raise ValueError("La cantidad de bultos debe ser mayor a cero.")
except ValueError as e:
    print(f"Error: {e}")
    exit()  # Finaliza el programa si hay un error en la cantidad de bultos

# Inicialización del contador
i = 0

while i < cantidadbultos:
    try:
        peso = int(input(f"Peso del bulto {i+1} (1-10 kg): "))
        if peso < 1 or peso > 10:
            raise ValueError("El peso debe estar entre 1 y 10 kg.")
        
        # Clasificación del bulto
        if peso <= 5:
            livianos += 1
        else:
            normales += 1
        
        i += 1  # Incrementamos el contador manualmente

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")

# Calcular el total a pagar
total_a_pagar = (livianos * 1000) + (normales * 2000)

# Mostrar el resumen
print("\nResumen del pedido:")
print(f"Bultos livianos: {livianos} - $ {livianos * 1000}")
print(f"Bultos normales: {normales} - $ {normales * 2000}")
print(f"Total a pagar: $ {total_a_pagar}")
