num = 7
factorial = 1

print("Ingresar un numero: ")
num = input()

if num < 0:
    print("El factorial no existe en los numeros negativos")
elif num == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("El factorial de ", num, "es", factorial)
