print("ingrese un numero")
num=int(input())

Funcion ={
1 : 'impar',
2 : 'par',
3 : 'impar' ,  
4 : 'par',
5 : 'impar',
6 : 'par',
7 : 'impar',
8 : 'par',
9 : 'impar',
10 : 'impar'    } 
print(Funcion.get(num, "este numero no esta en el rango permitido"))
