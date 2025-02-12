from modules.ControlPantalla import limpiar_pantalla,pausar
import modules.Menus as Menus
from modules.Diccionarios import libros,peliculas,musicas

def caso6(menu):
    limpiar_pantalla()
    print(menu)
    try:
        seleccion = int(input('Introduzca su selección: '))
    except ValueError:
        print('La opción no es válida')
        pausar()
        pass
    diccionarioLibros = {'Libros': libros}
    diccionarioPeliculas = {'Peliculas': peliculas}
    diccionarioMusicas = {'Musica': musicas}
    match seleccion:
        case 1:
            limpiar_pantalla()
            searchGenre = input('Introduzca el genero: ').strip().lower()
            for tipo, diccionario in diccionarioLibros.items():
                resultados = [item for item in diccionario.values() if item['Genero'].strip().lower() == searchGenre]
                if resultados:
                    print(f'Coincidencias en {tipo}:')
                    for resultado in resultados:
                        print(resultado)
                        pausar()
        case 2:
            limpiar_pantalla()
            searchGenre = input('Introduzca el genero: ').strip().lower()
            for tipo, diccionario in diccionarioPeliculas.items():
                resultados = [item for item in diccionario.values() if item['Genero'].strip().lower() == searchGenre]
                if resultados:
                    print(f'Coincidencias en {tipo}:')
                    for resultado in resultados:
                        print(resultado)
                        pausar()
        case 3:
            limpiar_pantalla()
            searchGenre = input('Introduzca el genero: ').strip().lower()
            for tipo, diccionario in diccionarioMusicas.items():
                resultados = [item for item in diccionario.values() if item['Genero'].strip().lower() == searchGenre]
                if resultados:
                    print(f'Coincidencias en {tipo}:')
                    for resultado in resultados:
                        print(resultado)
                        pausar()
        case 4:
            pass
        case _:
            print('La opcion no es valida, seleccione una del menu de opciones')
            pausar()