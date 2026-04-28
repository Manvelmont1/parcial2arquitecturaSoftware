## PUNTO 5: Alimentos que aportan mas de 1 mg de hierro y menos de 3 g de grasas
## Mapper - Lee todo el Dataset y filtra los alimentos que cumplen ambas condiciones

## Lectura del archivo
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lineas = open("./Dataset.csv", encoding="utf-8-sig").read().splitlines()
lineas = lineas[1:]  ## Eliminar encabezado

consolidado = {}

for linea in lineas:
    cols       = linea.split(";")
    alimento   = cols[0].strip()
    hierro_str = cols[5].strip().replace(",", ".")
    grasas_str = cols[3].strip().replace(",", ".")

    ## Ignorar valores no numericos (guiones)
    if hierro_str == "-": hierro_str = "0"
    if grasas_str == "-": grasas_str = "0"

    hierro = float(hierro_str)
    grasas = float(grasas_str)

    ## Solo incluir alimentos que cumplan ambas condiciones
    if hierro > 1 and grasas < 3:
        consolidado[alimento] = "hierro=" + str(hierro) + " grasas=" + str(grasas)

print(consolidado)

## Guardar resultado en un archivo para que el reducer pueda leerlo
resultado = ""

for clave in consolidado:
    resultado = resultado + str(clave) + ";" + str(consolidado[clave]) + "\n"

archivo = open("resultadoPunto5Mapper.csv", "w", encoding="utf-8")
archivo.write(resultado[:-1])  ## Elimina el ultimo caracter (en este caso es un salto de linea)
archivo.close()
