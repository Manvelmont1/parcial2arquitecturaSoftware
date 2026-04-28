## PUNTO 4: Alimento con mayor suma de vitaminas
## Vitaminas consideradas: Vitamina A [6], Tiamina B1 [7], Riboflavina B2 [8], Niacina [9], Vitamina C [10]
## Mapper - Lee todo el Dataset y calcula la suma de vitaminas de cada alimento

## Lectura del archivo
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8-sig").read().splitlines()
lineas = lineas[1:]  ## Eliminar encabezado

consolidado = {}

for linea in lineas:
    cols     = linea.split(";")
    alimento = cols[0].strip()

    vitA_str    = cols[6].strip().replace(",", ".")
    tiamina_str = cols[7].strip().replace(",", ".")
    ribofla_str = cols[8].strip().replace(",", ".")
    niacina_str = cols[9].strip().replace(",", ".")
    vitC_str    = cols[10].strip().replace(",", ".")

    ## Ignorar valores no numericos (guiones)
    if vitA_str    == "-": vitA_str    = "0"
    if tiamina_str == "-": tiamina_str = "0"
    if ribofla_str == "-": ribofla_str = "0"
    if niacina_str == "-": niacina_str = "0"
    if vitC_str    == "-": vitC_str    = "0"

    sumaVitaminas = float(vitA_str) + float(tiamina_str) + float(ribofla_str) + float(niacina_str) + float(vitC_str)

    consolidado[alimento] = sumaVitaminas

print(consolidado)

## Guardar resultado en un archivo para que el reducer pueda leerlo
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto4Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  ## Elimina el ultimo caracter (en este caso es un salto de linea)
archivo.close()
