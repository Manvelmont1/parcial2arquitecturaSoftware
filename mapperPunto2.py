# Alimento con mayor cantidad de vitamina C

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8").read().splitlines()
lineas = lineas[1:]  

consolidado = {}

for linea in lineas:
    alimento  = linea.split(";")[0].strip()
    vitC_str  = linea.split(";")[10].strip().replace(",", ".")

    if vitC_str == "-":
        vitC_str = "0"

    consolidado[alimento] = float(vitC_str)

print(consolidado)
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto2Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  
archivo.close()
