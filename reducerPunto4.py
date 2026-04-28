## PUNTO 4: Alimento con mayor suma de vitaminas
## Reducer - Lee el resultado del mapper y encuentra el alimento con mayor suma de vitaminas

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
resultadoMapper = open("./resultadoPunto4Mapper.csv", encoding="utf-8").read()
print(resultadoMapper)
print("--------------------------")

consolidado = {}

for linea in resultadoMapper.splitlines():
    alimento      = linea.split(";")[0]
    sumaVitaminas = float(linea.split(";")[1])
    consolidado[alimento] = sumaVitaminas

print(consolidado)

## Encontrar el alimento con mayor suma de vitaminas
alimentoMayorVitaminas = ""
maxSuma = -1

for clave in consolidado:
    if consolidado[clave] > maxSuma:
        alimentoMayorVitaminas = clave
        maxSuma = consolidado[clave]

resultado = "El alimento con mayor suma de vitaminas es: " + alimentoMayorVitaminas + " con una suma total de " + str(maxSuma)

print(resultado)

archivo = open("resultadoFinalPunto4.txt", "w", encoding="utf-8")
archivo.write(resultado)
archivo.close()
