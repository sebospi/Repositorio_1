num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

producto = 0
signo = 1

if num1 < 0:
    num1 = -num1
    signo = -signo

if num2 < 0:
    num2 = -num2
    signo = -signo

for _ in range(num2):
    producto += num1

producto *= signo
print("El producto de", num1, "y", num2, "es:", producto)
