numero = int(input("Ingrese un número: "))
divisor = 1

if numero == 0:
    print("Ningún número es divisible entre cero")
elif numero < 0:
    print("Ingrese un número positivo")
else:
    print("Divisores de", numero, ":")
    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
        divisor += 1
