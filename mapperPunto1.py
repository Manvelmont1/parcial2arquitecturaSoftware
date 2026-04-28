# Alimento con mayor cantidad de grasas

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8").read().splitlines()
lineas = lineas[1:] 

consolidado = {}

for linea in lineas:
    alimento  = linea.split(";")[0].strip()
    grasas_str = linea.split(";")[3].strip().replace(",", ".")

    if grasas_str == "-":
        grasas_str = "0"

    consolidado[alimento] = float(grasas_str)

print(consolidado)
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto1Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  
archivo.close()
