from grafo import Grafo

grafo = Grafo(dirigido = False)

def insert_vertice(grafo):
    grafo.insertar_vertice('Manjaro', {'tipo' : 'PC'})
    grafo.insertar_vertice('Parrot', {'tipo' : 'PC'})
    grafo.insertar_vertice('Fedora', {'tipo' : 'PC'})
    grafo.insertar_vertice('Mint', {'tipo' : 'PC'})
    grafo.insertar_vertice('Ubuntu', {'tipo' : 'PC'})
    grafo.insertar_vertice('Red Hat', {'tipo' : 'Notebook'})
    grafo.insertar_vertice('Debian', {'tipo' : 'Notebook'})
    grafo.insertar_vertice('Arch', {'tipo' : 'Notebook'})
    grafo.insertar_vertice('Impresora', {'tipo' : 'Impresora'})
    grafo.insertar_vertice('Guarani', {'tipo' : 'Servidor'})
    grafo.insertar_vertice('MongoDB', {'tipo' : 'Servidor'})
    grafo.insertar_vertice('Switch 1', {'tipo' : 'Switch'})
    grafo.insertar_vertice('Switch 2', {'tipo' : 'Switch'}) 
    grafo.insertar_vertice('Router 1', {'tipo' : 'Router'})
    grafo.insertar_vertice('Router 2', {'tipo' : 'Router'})
    grafo.insertar_vertice('Router 3', {'tipo' : 'Router'})

def insert_arista(grafo: Grafo):
    grafo.insertar_arista(40, 'Manjaro', 'Switch 2')
    grafo.insertar_arista(12, 'Parrot', 'Switch 2')
    grafo.insertar_arista(5, 'MongoDB', 'Switch 2')
    grafo.insertar_arista(56, 'Arch', 'Switch 2')
    grafo.insertar_arista(40, 'Fedora', 'Switch 2')
    grafo.insertar_arista(61, 'Switch 2', 'Router 3')
    grafo.insertar_arista(17, 'Debian', 'Switch 1')
    grafo.insertar_arista(18, 'Ubuntu', 'Switch 1')
    grafo.insertar_arista(22, 'Impresora', 'Switch 1')
    grafo.insertar_arista(80, 'Mint', 'Switch 1')
    grafo.insertar_arista(29, 'Switch 1', 'Router 1')
    grafo.insertar_arista(37, 'Router 1', 'Router 2')
    grafo.insertar_arista(43, 'Router 1', 'Router 3')
    grafo.insertar_arista(50, 'Router 3', 'Router 2')
    grafo.insertar_arista(25, 'Red Hat', 'Router 2')
    grafo.insertar_arista(9, 'Guarani', 'Router 2')

def camino_corto(grafo, origen, destino): # Busca el camino mas corto entre dos vertices
    vertice_origen = grafo.buscar_vertice(origen)
    vertice_destino = grafo.buscar_vertice(destino) # Primero busca los vertices, si estan, se realiza lo siguiente
    costo = None

    if vertice_origen != -1 and vertice_destino != -1:
        camino = grafo.dijkstra(vertice_origen)
        while not camino.pila_vacia():
            dato = camino.desapilar()
            if dato[1][0] == destino:
                if costo is None:
                    costo = dato[0]
                print('paso por', dato[1][0])
                destino = dato[1][1]
        print('Camino mas corto:', costo)

def cambiar_visitado(grafo, origen = 0):
    while origen < grafo.inicio.tamanio():
        vertice = grafo.inicio.obtener_elemento(origen)
        if vertice['visitado']:
            vertice['visitado'] = False
            aristas = 0
            while aristas < vertice['aristas'].tamanio():
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos = grafo.buscar_vertice(arista['destino'])
                nuevo_vertice = grafo.inicio.obtener_elemento(pos)
                if nuevo_vertice['visitado']:
                    cambiar_visitado(grafo, pos)
                aristas += 1
        origen += 1 

def barrido_en_profundidad(grafo, nombre): # Barrido en profundidad
    pos = grafo.buscar_vertice(nombre)
    
    if pos != -1:
        grafo.barrido_profundidad(pos)
        cambiar_visitado(grafo)
    else:
        print(nombre, 'no existe')

# PUNTO 1
insert_vertice(grafo)
insert_arista(grafo)


print('\nBarrido en profundidad desde Red Hat:') # PUNTO 2
barrido_en_profundidad(grafo, 'Red Hat')
print('\nBarrido en profundidad desde Debian:')
barrido_en_profundidad(grafo, 'Debian')
print('\nBarrido en profundidad desde Arch:')
barrido_en_profundidad(grafo, 'Arch')

print('\nCamino mas corto de Debian a MongoDB') # PUNTO 3
camino_corto(grafo, 'Debian', 'MongoDB')
print('\nCamino mas corto de Red Hat a MongoDB')
camino_corto(grafo, 'Red Hat', 'MongoDB')

print('\nArbol de expansion minima')
grafo.prim()

grafo.eliminar_vertice('Impresora') # PUNTO 5
print('\nBarrido sin la impresora') # Muestra como quedaria eliminando impresora