
print("Ingrese  el ano")
ano=int(input())
if (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0):
    print ("El ano es BISIESTO")
else:
    print ("El ano NO es BISIESTO")
