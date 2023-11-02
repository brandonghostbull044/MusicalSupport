import os
import shutil

archivo = open('Partituras.txt', 'r').read()
instrumentos = archivo.split('@')
cancionesArmonica = instrumentos[0].split('*')[1:]
partitura1 = cancionesArmonica[0].split('|')[1].split('°')
for i in partitura1:
    print(i)
