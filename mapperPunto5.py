# Alimentos con mas de 1 mg de hierro y menos de 3 gr de grasas

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8-sig").read().splitlines()
lineas = lineas[1:]  

consolidado = {}

for linea in lineas:
    cols       = linea.split(";")
    alimento   = cols[0].strip()
    hierro_str = cols[5].strip().replace(",", ".")
    grasas_str = cols[3].strip().replace(",", ".")

    if hierro_str == "-": hierro_str = "0"
    if grasas_str == "-": grasas_str = "0"

    hierro = float(hierro_str)
    grasas = float(grasas_str)

    if hierro > 1 and grasas < 3:
        consolidado[alimento] = "hierro=" + str(hierro) + " grasas=" + str(grasas)

print(consolidado)
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto5Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1]) 
archivo.close()
