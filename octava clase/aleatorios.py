import random

def generar_lista_numeros_aleatorios(n):
    lista = [random.randint(1, 100) for _ in range(n)]
    return lista

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

if __name__ == "__main__":
    cantidad_numeros = 15

    numeros_aleatorios = generar_lista_numeros_aleatorios(cantidad_numeros)

    print("Lista original de números aleatorios:")
    print(numeros_aleatorios)

    lista_ordenada = ordenar_lista(numeros_aleatorios)
    print("\nLista ordenada de menor a mayor:")
    print(lista_ordenada)
