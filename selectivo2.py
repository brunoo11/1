print("Ingrese su sueldo ")
x = int(input())
if x<=999:
    aumento = x*0.15
    total = x + aumento
    print("el trabajador merece el aumento, su sueldo ahora sera de ", total)
else:
    print("el trabajador gana demasiado para recibir un aumento")