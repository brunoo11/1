pi = 3.1416
print("Ingrese Radio y el Alto ")
radio = float( input("Radio "))
alto = float ( input("Alto "))
vol = pi * radio**2 * alto
are = 2*pi*radio*(radio + alto)
print("Volumen ", vol)
print("área ", are)