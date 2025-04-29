total_ingresos=0
nro_pasaje_vender=int(input("Cuantos pasajes quieres vender?: "))
for i in range(nro_pasaje_vender):
    valor=int(input(f"Valor de cada pasaje {i+1}: "))
    total_ingresos += valor
    
     
print(f"Total a pagar: {total_ingresos}")

