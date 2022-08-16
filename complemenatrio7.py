import math
print("ingrese los lados del triangulo")
b = float( input("Lado b: "))
c = float( input("Lado c: "))
print("Ingrese el ángulo en grados sexagesimales:")
alfa = float( input())
pi=3.14
a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*pi/180 ) )**0.50