# Alimento con mayor suma de vitaminas

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8-sig").read().splitlines()
lineas = lineas[1:]

consolidado = {}

for linea in lineas:
    cols     = linea.split(";")
    alimento = cols[0].strip()

    vitA_str    = cols[6].strip().replace(",", ".")
    tiamina_str = cols[7].strip().replace(",", ".")
    ribofla_str = cols[8].strip().replace(",", ".")
    niacina_str = cols[9].strip().replace(",", ".")
    vitC_str    = cols[10].strip().replace(",", ".")

    if vitA_str    == "-": vitA_str    = "0"
    if tiamina_str == "-": tiamina_str = "0"
    if ribofla_str == "-": ribofla_str = "0"
    if niacina_str == "-": niacina_str = "0"
    if vitC_str    == "-": vitC_str    = "0"

    sumaVitaminas = float(vitA_str) + float(tiamina_str) + float(ribofla_str) + float(niacina_str) + float(vitC_str)
    consolidado[alimento] = sumaVitaminas

print(consolidado)
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto4Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  
archivo.close()
