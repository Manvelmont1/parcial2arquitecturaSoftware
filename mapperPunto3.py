## N. de alimentos que tienen mas de 0.1 gramos de tiamina

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8").read().splitlines()
lineas = lineas[1:]

consolidado = {
    "cantidad": 0
}

for linea in lineas:
    tiamina_str = linea.split(";")[7].strip().replace(",", ".")

    if tiamina_str == "-":
        tiamina_str = "0"

    tiamina = float(tiamina_str)

    if tiamina > 0.1:
        consolidado["cantidad"] = consolidado["cantidad"] + 1

print(consolidado)
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto3Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1]) 
archivo.close()
