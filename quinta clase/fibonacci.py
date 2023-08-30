n = int(input("Ingrese la cantidad de dígitos de la serie de Fibonacci que desea mostrar: "))

a, b = 0, 1

print("Serie de Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
