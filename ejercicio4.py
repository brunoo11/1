print("Ingrese número de partidos ganados")
pg = int( input())
print("Ingrese número de partidos empatados")
pe = int( input())
print("Ingrese número de partidos perdidos")
pp = int( input())
#Proceso
ppg = pg*3
ppe = pe*1
ppp = pp*0
pf = ppg + ppe + ppp

print("el puntaje es" )
print(pf)