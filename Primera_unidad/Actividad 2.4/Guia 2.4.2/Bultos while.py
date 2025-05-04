livianos=0
normales=0
total_a_pagar= 0
try:
    cantidadbultos=int(input("Cuantos bultos desea registrar: "))
except ValueError:
    print("Error: Debe ingresar un numero entero.")
    cantidadbultos=0
if cantidadbultos <= 0:
    raise ValueError("Error: La cantidad de bultos debe ser mayor a cero.")
i=0
while i < cantidadbultos:
    peso=int(input(f"Peso del bulto?(1-10kg) {i+1}: "))
    if peso >=1 and peso <= 5:
        livianos += 1
    elif peso >= 6 and peso <= 10:
        normales += 1
    else:
        print("El peso pasa los kg estipulados")
    i += 1
total_a_pagar=(livianos * 1000) + (normales * 2000)

print(f"{livianos} Bultos livianos ${livianos*1000}")
print(f"{normales} Bultos normales ${normales*2000}")
print(f"Total a pagar: ${total_a_pagar}")