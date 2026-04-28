## PUNTO 2: Alimento con mayor cantidad de vitamina C
## Mapper - Lee todo el Dataset y extrae el nombre y la vitamina C de cada alimento

## Lectura del archivo
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8").read().splitlines()
lineas = lineas[1:]  ## Eliminar encabezado

consolidado = {}

for linea in lineas:
    alimento  = linea.split(";")[0].strip()
    vitC_str  = linea.split(";")[10].strip().replace(",", ".")

    ## Ignorar valores no numericos (guiones)
    if vitC_str == "-":
        vitC_str = "0"

    consolidado[alimento] = float(vitC_str)

print(consolidado)

## Guardar resultado en un archivo para que el reducer pueda leerlo
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto2Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  ## Elimina el ultimo caracter (en este caso es un salto de linea)
archivo.close()
