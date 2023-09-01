def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

if __name__ == "__main__":
    cantidad_numeros_perfectos = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))

    numeros_perfectos_encontrados = 0
    numero_actual = 1

    while numeros_perfectos_encontrados < cantidad_numeros_perfectos and numero_actual <= 10000:  # Límite para evitar bucle infinito
        if es_numero_perfecto(numero_actual):
            print(f"Número perfecto encontrado: {numero_actual}")
            numeros_perfectos_encontrados += 1

        numero_actual += 1

