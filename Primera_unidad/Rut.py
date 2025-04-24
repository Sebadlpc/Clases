print("Este programa sirve para validar un RUT")
print("Por favor, ingrese el RUT sin puntos y guion")
rut=input("Ingrese el RUT a validar: ").replace(".","").replace("-","").strip().upper()
rut_invertido=rut[::-1]
print(rut_invertido)
   
num1=int(rut_invertido[1])*2
num2=int(rut_invertido[2])*3
num3=int(rut_invertido[3])*4
num4=int(rut_invertido[4])*5
num5=int(rut_invertido[5])*6
num6=int(rut_invertido[6])*7
num7=int(rut_invertido[7])*2
num8=int(rut_invertido[8])*3
paso4=int(num1+num2+num3+num4+num5+num6+num7+num8)
paso5=int(paso4/11)
paso6=int(paso5*11)
paso7=int(paso4-paso6)
paso8=int(11-paso7)
print(paso8)

if paso8==10:
     paso8="K"
elif paso8==11:
     paso8="0"

if str(paso8).upper() == str(rut_invertido[0]).upper():
     print("El RUT es válido")
else: 
     print("El RUT no es valido")