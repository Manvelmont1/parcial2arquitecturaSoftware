# Alimento con mayor cantidad de vitamina C

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
resultadoMapper = open("./resultadoPunto2Mapper.csv", encoding="utf-8").read()
print(resultadoMapper)
print("--------------------------")

consolidado = {}

for linea in resultadoMapper.splitlines():
    alimento = linea.split(";")[0]
    vitC     = float(linea.split(";")[1])
    consolidado[alimento] = vitC

print(consolidado)
alimentoMayorVitC = ""
maxVitC = -1

for clave in consolidado:
    if consolidado[clave] > maxVitC:
        alimentoMayorVitC = clave
        maxVitC = consolidado[clave]

resultado = "El alimento con mayor cantidad de vitamina C es: " + alimentoMayorVitC + ": " + str(maxVitC) + " mg"

print(resultado)

archivo = open("resultadoPunto2.txt", "w", encoding="utf-8")
archivo.write(resultado)
archivo.close()
