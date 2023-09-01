def ingresar_numeros_hasta_negativo():
    lista_numeros = []
    while True:
        numero = int(input("Ingrese un número (o un número negativo para terminar): "))
        if numero < 0:
            break
        lista_numeros.append(numero)
    return lista_numeros

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

if __name__ == "__main__":
    print("Ingrese números. Ingrese un número negativo para finalizar.")

    lista_original = ingresar_numeros_hasta_negativo()

    print("\nLista original:")
    print(lista_original)

    lista_sin_duplicados = eliminar_duplicados(lista_original)

    # Imprime la lista sin duplicados.
    print("\nLista sin duplicados:")
    print(lista_sin_duplicados)
