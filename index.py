from Musica import Musica
from partituras import partituras

print('Bienvenido.')
   
while True:
    peticion = input('\n¿En qué puedo ayudarte?.\n     a)Escribir una partitura.\n     b)Consultar una partitura.\n\nTambién puedes "Exit" para cerrar el progrma.\n--> ')
    if peticion.lower() == 'a':
        Musica().escribirPartitura()
    elif peticion.lower() == 'b':
        Musica().consultarpartitura()
    elif peticion.lower() == "exit":
        print('\n                Adios.\n')
        break
    else:
        print('\n\nError de escritura.\n\n')