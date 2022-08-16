print("Ingrese las coordenadas del Punto A: ")
ax = float(input("Ax "))
ay = float(input("Ay "))
print("Ingrese las coordenadas del Punto B: ")
bx = float(input("Bx "))
by = float(input("By "))
D = ( (ax-bx)**2 + (ay-by)**2 )**0.5
print(D)