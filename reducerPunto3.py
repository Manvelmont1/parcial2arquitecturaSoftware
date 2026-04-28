# N. de alimentos que tienen mas de 0.1 gramos de tiamina

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
resultadoMapper = open("./resultadoPunto3Mapper.csv", encoding="utf-8").read()
print(resultadoMapper)
print("--------------------------")

consolidado = {
    "cantidad": 0
}

for linea in resultadoMapper.splitlines():
    clave = linea.split(";")[0]
    valor = int(linea.split(";")[1])
    consolidado[clave] = consolidado[clave] + valor

print(consolidado)
resultado = "La cantidad de alimentos con mas de 0.1 gramos de tiamina es: " + str(consolidado["cantidad"])

print(resultado)

archivo = open("resultadoPunto3.txt", "w", encoding="utf-8")
archivo.write(resultado)
archivo.close()
