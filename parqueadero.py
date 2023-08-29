n= int(input("Ingrese el tiempo que duró en el parqueadero (Sólo el valor numerico): "))
r= input("El tiempo está en minutos (m) u horas (h):")
horas = "h"
minutos = "m"
if r == horas:
    h = round((n*60) * 139) 
    ih = round(h * 0.19) 
    th = round(h + ih) 
    print("Usted estuvo", n," hora(s), por lo tanto tiene que pagar: \n Total sin IVA: ", h,"\n IVA: ", ih,"\
          \n Total con IVA: ", th )
elif r == minutos: 
    m = round(n * 139)
    im = round(m * 0.19)
    tm = round(m + im)
    print("Usted estuvo", n," minuto(s), por lo tanto tiene que pagar: \n Total sin IVA: ", m,"\n IVA: ", im,"\
          \n  Total con IVA: ", tm )
else:
    print("Ingrese una hora válida")
    


