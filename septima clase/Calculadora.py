import math

def calcular_modulo(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    modulo = math.sqrt(dx**2 + dy**2)

    return modulo, dx, dy

if __name__ == "__main__":
    x1 = float(input("Ingrese la coordenada x del punto de origen: "))
    y1 = float(input("Ingrese la coordenada y del punto de origen: "))
    x2 = float(input("Ingrese la coordenada x del punto de destino: "))
    y2 = float(input("Ingrese la coordenada y del punto de destino: "))

    modulo, dx, dy = calcular_modulo(x1, y1, x2, y2)

    print(f"El módulo del vector es: {modulo}")
    print(f"Las componentes rectangulares son: ({dx}, {dy})")

