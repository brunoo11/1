print("ingrese un tipo de calculo")
num=int(input())
print("ingrese un numero")
v=int(input())
Funcion ={
1 : 100*v,
2 : 100**v,
3 : 100/v   }
VAL = Funcion.get(num, 0)
print(VAL)
