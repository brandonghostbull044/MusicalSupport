from Musica import Musica

print('Bienvenido.')
   
while True:
    peticion = input('\n¿En qué puedo ayudarte?.\n     a)Escribir una partitura.\n     b)Consultar una partitura.\n\nTambién puedes "Exit" para cerrar el programa.\n--> ')
    iniciar = Musica()
    iniciar.definir()
    if peticion.lower() == 'a':
        iniciar.escribirPartitura()
    elif peticion.lower() == 'b':
        iniciar.consultarpartitura()
    elif peticion.lower() == "exit":
        print('\n                Adios.\n')
        break
    else:
        print('\n\nError de escritura.\n\n')