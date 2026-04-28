## PUNTO 1: Alimento con mayor cantidad de grasas
## Mapper - Lee todo el Dataset y extrae el nombre y las grasas de cada alimento

## Lectura del archivo
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8").read().splitlines()
lineas = lineas[1:]  ## Eliminar encabezado

consolidado = {}

for linea in lineas:
    alimento  = linea.split(";")[0].strip()
    grasas_str = linea.split(";")[3].strip().replace(",", ".")

    ## Ignorar valores no numericos (guiones)
    if grasas_str == "-":
        grasas_str = "0"

    consolidado[alimento] = float(grasas_str)

print(consolidado)

## Guardar resultado en un archivo para que el reducer pueda leerlo
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto1Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  ## Elimina el ultimo caracter (en este caso es un salto de linea)
archivo.close()
