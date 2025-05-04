subsidio= 0
print("Q1=Ingresos bajos \n"
      "Q2=Ingresos medios/bajos \n"
      "Q3=Ingresos medios \n"
      "Q4=Ingresos medios/altos \n"
      "Q5=Ingresos altos")
quintil=int(input("¿A que quintil perteneces? (1-5): "))
CL=input("¿Condicion laboral?: ")
edad=int(input("¿Cual es su edad?: "))

if quintil == 1 or quintil == 2 and CL == "desempleado":
    subsidio += 10000
elif quintil == 1 or quintil == 2 and CL == "empleado":
    subsidio += 8000
elif quintil == 3 and CL == "desempleado":
    subsidio += 6000
elif quintil == 3 and CL == "empleado":
    subsidio += 4000
elif quintil == 4 or quintil == 5 and CL == "desempleado" or CL == "empleado":
    subsidio += 1500

if edad >= 65:
    subsidio += 3000
if quintil == 1 or quintil == 2:
    subsidio += 2000

print(f"Su subsidio es de: ${subsidio}")