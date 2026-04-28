## PUNTO 1: Alimento con mayor cantidad de grasas
## Reducer - Lee el resultado del mapper y encuentra el alimento con mayor grasas

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
resultadoMapper = open("./resultadoPunto1Mapper.csv", encoding="utf-8").read()
...
print(resultadoMapper)
print("".center(50, "-"))

consolidado = {}

for linea in resultadoMapper.splitlines():
    alimento = linea.split(";")[0]
    grasas   = float(linea.split(";")[1])
    consolidado[alimento] = grasas

print(consolidado)

## Encontrar el maximo de grasas
maxGrasas = -1

for clave in consolidado:
    if consolidado[clave] > maxGrasas:
        maxGrasas = consolidado[clave]

## Recopilar todos los alimentos que tienen ese maximo
alimentosConMaximo = []

for clave in consolidado:
    if consolidado[clave] == maxGrasas:
        alimentosConMaximo.append(clave)

resultado = "Los alimentos con mayor cantidad de grasas (" + str(maxGrasas) + " gr) son: " + ", ".join(alimentosConMaximo)

print(resultado)

archivo = open("resultadoPunto1.txt", "w", encoding="utf-8")
archivo.write(resultado)
archivo.close()
