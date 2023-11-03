partituras = open('Partituras.txt', 'r').read()

class Musica:
    def __init__(self):
        self.partituras = {}
        
    def definir(self):
        for i in partituras.split('@'):
            instrumento = i.split('*')[0]
            self.partituras[instrumento] = {}
            for a in i.split('*')[1:]:
                sing = a.split('|')[0]
                partitura = a.split('|')[1:]
                self.partituras[instrumento][sing] = partitura           
            
    def consultarpartitura(self):
        while True:
            instrumento = input('\n\n¿De qué instrumento?. Puedes listar los instrumentos escribiendo "List" o escribe "Exit" para salir de la consulta de partituras.--> ').lower()
            if instrumento != 'list' and instrumento != 'exit' and instrumento.capitalize() in list(self.partituras.keys()):
                while True:
                    cancion = input('\n\nIngresa el nombre de la canción que quieres. Puedes listar los nombres de las canciones ingresando "List" o si quieres cambiar de instrumento ingresa "Change". --> ').lower()
                    if cancion != 'list' and cancion != 'change':
                        confirmacion = bool
                        cancionesEncontradas = []
                        canciones = list(self.partituras[instrumento.capitalize()].keys())
                        for sing in canciones:
                            if cancion in sing.lower():
                                cancionesEncontradas.append(sing)
                                confirmacion = True
                        if confirmacion and len(cancionesEncontradas) > 1:
                            print('\n\nAquí tienes algunas coincidencias con tu busqueda: ')
                            for sing in cancionesEncontradas:
                                print(f'     {cancionesEncontradas.index(sing) + 1}) {sing}')
                            busqueda = cancionesEncontradas[int(input('\n\nIngresa el número de la cancion que quieres.--> ')) - 1]
                            partitura = self.partituras[instrumento][busqueda]
                            print(f'\n\n          {busqueda}')
                            for line in partitura[0].split('°'):
                                print(f'\n\n          {line}')
                            print(f'\n\n     Link a la clase: {partitura[1]}')
                            
                        elif confirmacion and len(cancionesEncontradas) == 1:
                            busqueda = cancionesEncontradas[0]
                            partitura = self.partituras[instrumento.capitalize()][busqueda]
                            print(f'\n\n          "{busqueda}"\n')
                            for line in partitura[0].split('°'):
                                print(f'\n          {line}')
                            print(f'\n\n     Link a la clase: {partitura[1]}')
                            
                        else:
                            print('No tengo la canción que buscas')
                    elif cancion == 'list':
                        for sing in list(self.partituras[instrumento.capitalize()].keys()):
                            print(f'\n\n     {sing}')
                    elif cancion == 'change':
                        break
                    else:
                        print('\n\nError de escritura.')
                        
            elif instrumento != 'list' and instrumento != 'exit' and instrumento.capitalize() not in list(self.partituras.keys()):
                print('\n\nAún no cuento partituras de ese instrumento.\n\n')
                
            elif instrumento == 'list':
                for inst in list(self.partituras.keys()):
                    print(f'\n\n     {inst}')
            
            elif instrumento == 'exit':
                break