#Ejercicio 3: Factorial

# Función para calcular potencia: x^exponente
def potencia(x, exponente):
    rta = 1
    for i in range(1, exponente + 1):
        rta = rta * x
    return rta


def factorial(num):
    rta = 1
    for i in range(1, num + 1):
        rta = rta * i
    return rta

print("Bienvenido")
print("Obtendremos una aproximación a la función e^x")
print("a partir de un x ingresado y un n que define la exactitud")
print()

x = float(input("Digite x (exponente de la función exponencial natural): "))
n = int(input("Digite n (exactitud de la respuesta): "))

rta = 1

for i in range(1, n + 1):
    rta = rta + (potencia(x, i) / factorial(i))

print(f"La rta de e^{x} es: {rta}")
