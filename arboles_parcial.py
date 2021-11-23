from arboles import Arbol

arbol_nombre = Arbol()
arbol_codigo = Arbol()

dinos = [
			{'name': 'T-rex', 'codigo': '00192', 'zona': '7A'},
			{'name': 'Sgimoloch', 'codigo': '00912', 'zona': '4A'},
			{'name': 'Velociraptor', 'codigo': '00324', 'zona': '4B'},
			{'name': 'Triceratops', 'codigo': '00155', 'zona': '4C'},
			{'name': 'Diplodocus', 'codigo': '00323', 'zona': '9A'},
			{'name': 'Braquiosaurio', 'codigo': '00792', 'zona': '5C'},
			{'name': 'Estegosaurio', 'codigo': '00121', 'zona': '2C'},
			{'name': 'Iguanodonte', 'codigo': '01204', 'zona': '9C'},
			{'name': 'Arqueopterix', 'codigo': '00423', 'zona': '8B'},
			{'name': 'Protoceratops', 'codigo': '00420', 'zona': '7A'},
			{'name': 'Raptor', 'codigo': '00253', 'zona': '2A'},
			{'name': 'T-rex', 'codigo': '00182', 'zona': '3B'},
			{'name': 'Anquilosaurio', 'codigo': '00344', 'zona': '6A'},
			{'name': 'Raptor', 'codigo': '00455', 'zona': '1B'},
			{'name': 'T-rex', 'codigo': '00626', 'zona': '2B'},
			{'name': 'Diplodocus', 'codigo': '05626', 'zona': '1D'},

        ]

def dino_info_nombre(arbol_nombre, nombre): # Busca el dinosaurio segun el nombre y muestra su info
	if arbol_nombre.info is not None:
		if arbol_nombre.datos['name'] == nombre:
			print(arbol_nombre.info, arbol_nombre.datos)
		if arbol_nombre.izq is not None:
			dino_info_nombre(arbol_nombre.izq, nombre)
		if arbol_nombre.der is not None:
			dino_info_nombre(arbol_nombre.der, nombre)

def cambiarNombre(arbol, buscado, codigo):
    pos = arbol.busqueda(buscado)
    if pos is not None:
        print('Datos del dinosaurio:', pos.datos)
        nuevo_nombre = ('Stygimoloch') # Se reemplaza el nombre

        pos.datos['name'] = nuevo_nombre

        if arbol == arbol_nombre:	        	
	        pos.info = nuevo_nombre

        print('Nuevos datos del dinosaurio',pos.info, pos.datos)
        print('Nuevo nombre en arbol codigo', arbol_codigo.busqueda(codigo).info, arbol_codigo.busqueda(codigo).datos)        
    else:
        print(buscado,'no se encuentra en el arbol')

def cant_tipo_dino(arbol, nombre):
	cont = 0
	if arbol.info is not None:
		if arbol.datos['name'] == nombre:
			cont += 1
		if arbol.izq is not None:
			cont += cant_tipo_dino(arbol.izq, nombre)
		if arbol.der is not None:
			cont += cant_tipo_dino(arbol.der, nombre)

	return cont

def zona_dinos(arbol, nombre):
	if arbol.info is not None:
		if arbol.datos['name'] == 'Raptor':
			print(arbol.datos['zona'])
		if arbol.izq is not None:
			zona_dinos(arbol.izq, nombre)
		if arbol.der is not None:
			zona_dinos(arbol.der, nombre)

# Cargo los dinosaurios en un arbol por nombre, y en otro por codigo ------ PUNTO 2
arbol_nombre = arbol_nombre.cargar_arbol(dinos, 'name')
arbol_codigo = arbol_codigo.cargar_arbol(dinos, 'codigo') 

print('Barrido en orden de los dinosaurios:')
arbol_nombre.inorden() # Barrido en orden por nombre ------- PUNTO 3

print('Punto 4')
print(arbol_codigo.busqueda('00792').datos) # ------ PUNTO 4

print()
print('Todos los t-rex: ')
dino_info_nombre(arbol_nombre, 'T-rex') # ------ PUNTO 5

print()
cambiarNombre(arbol_nombre, 'Sgimoloch', '00912') # Cambio nombre en arbol por nombre ------ PUNTO 6
print()

print('Ubicacion de raptores:') # Muestra ubicacion de los raptores ------- PUNTO 7
zona_dinos(arbol_nombre, 'Raptor')

print()
print('Cantidad de Diplodocus',cant_tipo_dino(arbol_nombre, 'Diplodocus')) # ------ PUNTO 8
