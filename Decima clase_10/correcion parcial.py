

from random import uniform as u 

def rates():
    comision=[]
    for i in range(5):
        comision.append(round(u(0.1,0.5),2))
    #print(comision)
    return comision 


def ver_tasas(r,d,c):
    for i in range(5):
        print (f"divisa: {d[i]}, tasa: {c[i]}, comision: {r[i]}")


def conversion(r,d,c):
    divisa= input("A que divisa desea hacer el cambio: ").upper()
    if divisa in d:
        idx=d.index(divisa)
        divisa= (d[idx])
        tasa= int(c[idx])
        comision= r[idx]
        precio_venta=tasa+(tasa*comision)
        cambio=int(input("Que valor desea cambiar: "))
        total= cambio// precio_venta
        vueltas=round((cambio - precio_venta*total),2)
        print(f"Cambio: {total} {divisa}, devolucion: {vueltas} COP ")
        return 1
    print("Ingrese un valor válido")


def menu():
    comision= rates()
    divisa=["USD","EUR","CNY","JPY","PEN"]
    cambios=[ "4108","4544","563 ","28  ","1106"]
    print("Seleccione una de las siguientes opciones\n",
          "1. Cambio de divisas\n","2. Ver tasas de cambio\n","3. Salir")
    opc=input("Seleccione una opcion: ")

    while opc!="salir":
        if opc=="1":
            conversion(comision,divisa,cambios)
        elif opc=="2":
            ver_tasas(comision,divisa,cambios)
        elif opc=="Salir" or 3:
            break
        else:
            print("Seleccion invalida")
        opc=input("Seleccione una opcion")


def inicio():
    menu()


if __name__=="__main__":
    inicio()