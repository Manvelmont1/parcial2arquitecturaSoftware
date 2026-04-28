## PUNTO 3: Cuantos alimentos tienen mas de 0.1 gramos de tiamina
## Mapper - Lee todo el Dataset y cuenta los alimentos que cumplen la condicion

## Lectura del archivo
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8").read().splitlines()
lineas = lineas[1:]  ## Eliminar encabezado

consolidado = {
    "cantidad": 0
}

for linea in lineas:
    tiamina_str = linea.split(";")[7].strip().replace(",", ".")

    ## Ignorar valores no numericos (guiones)
    if tiamina_str == "-":
        tiamina_str = "0"

    tiamina = float(tiamina_str)

    if tiamina > 0.1:
        consolidado["cantidad"] = consolidado["cantidad"] + 1

print(consolidado)

## Guardar resultado en un archivo para que el reducer pueda leerlo
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto3Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  ## Elimina el ultimo caracter (en este caso es un salto de linea)
archivo.close()
