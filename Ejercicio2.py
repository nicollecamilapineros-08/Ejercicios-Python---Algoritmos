#Ejercicio 2: Numeros primos
def construir_cadena(lim):
    cad = ""
    for x in range(2, lim+1):
        cad += f"{x},"
    return cad.rstrip(",")

def quitar_cadena(str, num):
    cad = ""
    for n in str.split(","):
        if n != num:
            if int(n) % int(num) != 0:
                cad += f"{n},"
        else:
            cad += f"{n},"

    return cad.rstrip(",")



lim= 1000
str = construir_cadena(lim)
for snum in str.split(","):
    str= quitar_cadena(str, snum)

print(str)
