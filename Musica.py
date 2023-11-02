from partituras import partituras

class Musica:
    def __init__(self):
        pass
    
    def consultarpartitura(self):
        while True:
            instrumento = input('\n¿De qué instrumento?. Puedes listar los instrumentos escribiendo "List" o escribe "Exit" para salir de la consulta de partituras.--> ').lower()
            if instrumento in partituras:
                canciones = list(partituras[instrumento])
                while True:
                    cancion = input('\n\n¿Cuál canción quieres?. Puedes listar las canciones escribiendo "List" o escribe "Change" para cambiar de instrumento.\n\n-->')
                    if cancion.lower() != 'list' and cancion.lower() != 'change': 
                        cancionesEncontradas = []
                        for single in canciones:
                            if cancion.lower() in single.lower():
                                cancionesEncontradas.append(single)
                        if len(cancionesEncontradas) > 1:
                            contador = 0
                            print('Aquí algunas coicidencias con tu busqueda:')
                            for single in cancionesEncontradas:
                                print(f'\n    {contador + 1}) {cancionesEncontradas[contador]}')
                                contador += 1
                            try:
                                print(f'{partituras[instrumento][cancionesEncontradas[int(input("Ingresa el número de la canción que quieras. --> "))]]}')
                            except:
                                print('Error de escritura.')
                        elif len(cancionesEncontradas) == 1:
                            print(f'\n{cancionesEncontradas[0]}\n\n{partituras[instrumento][cancionesEncontradas[0]].split("@")[0]}\n\nLink a la clase: {partituras[instrumento][cancionesEncontradas[0]].split("@")[1]}')
                        else:
                            print('\nLa canción que buscas no la tengo.\n')
                    elif cancion.lower() == 'change':
                        break
                    else: 
                        for single in canciones:
                            print(f'\n    {single}\n')
            elif instrumento == 'list':
                for instrumento in partituras:
                    print(f'\n    {instrumento.capitalize()}\n')
            elif instrumento == 'exit':
                break
    
    def escribirPartitura(self):
        pass