# Ejercicio 1: Capital final

print("Bienvenido")

capital = float(input("Ingrese el capital inicial: "))
anios = int(input("Ingrese el tiempo estimado a pagar (años): "))
interes = float(input("Ingrese el valor del interés propuesto (%): "))

# Validación del interés
if interes < 0 or interes > 100:
    print("No es posible hacer el cálculo, valor de interés inválido.")
else:
    valor_final = capital

    for x in range(1, anios + 1):
        valor_final = valor_final * (1 + interes / 100)

    print("El valor final de su capital es de:", round(valor_final, 2))

