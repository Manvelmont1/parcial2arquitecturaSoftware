# Alimentos con mas de 1 mg de hierro y menos de 3 gr de grasas

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
resultadoMapper = open("./resultadoPunto5Mapper.csv", encoding="utf-8").read()
print(resultadoMapper)
print("--------------------------")

consolidado = {}

for linea in resultadoMapper.splitlines():
    alimento = linea.split(";")[0]
    detalle  = linea.split(";")[1]
    consolidado[alimento] = detalle

print(consolidado)

listaAlimentos = ""
for clave in consolidado:
    listaAlimentos = listaAlimentos + "- " + clave + " (" + consolidado[clave] + ")\n"

resultado = "Alimentos con mas de 1 mg de hierro y menos de 3 g de grasas:\n" + listaAlimentos.strip()

print(resultado)

archivo = open("resultadoFinalPunto5.txt", "w", encoding="utf-8")
archivo.write(resultado)
archivo.close()
