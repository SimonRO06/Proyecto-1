from modules.ControlPantalla import limpiar_pantalla,pausar
import modules.Menus as Menus
from modules.Diccionarios import libros,peliculas,musicas
# Buscar un Elemento:
def caso3(menu):
    limpiar_pantalla()
    print(menu)
    try:
        seleccion = int(input('Introduzca su selección: '))
    except ValueError:
        print('La opción no es válida')
        pausar()
        pass
    diccionarios = {'Libros': libros, 'Peliculas': peliculas, 'Musica': musicas}
    match seleccion:
        case 1:
            limpiar_pantalla()
            searchName = input('Introduzca el nombre del elemento a buscar: ').strip().lower()
            for categoria, diccionario in diccionarios.items():
                resultados = [item for v, item in diccionario.values() if item['Nombre'].strip().lower() == searchName]
                if resultados:
                    print(f'Coincidencias en {categoria}:')
                    for resultado in resultados:
                        print(resultado)
                        pausar()
        case 2:
            limpiar_pantalla()
            searchAuthor = input('Introduzca el nombre del autor/director/artista: ').strip().lower()
            for categoria, diccionario in diccionarios.items():
                resultados = [item for item in diccionario.values() if item['Autor'].strip().lower() == searchAuthor]
                if resultados:
                    print(f'Coincidencias en {categoria}:')
                    for resultado in resultados:
                        print(resultado)
                        pausar()
        case 3:
            limpiar_pantalla()
            searchGenre = input('Introduzca el genero: ').strip().lower()
            for categoria, diccionario in diccionarios.items():
                resultados = [item for item in diccionario.values() if item['Genero'].strip().lower() == searchGenre]
                if resultados:
                    print(f'Coincidencias en {categoria}:')
                    for resultado in resultados:
                        print(resultado)
                        pausar()
        case 4:
            pass
        case _:
            print('La opción no es valida, seleccione una del menu de opciones')
            pausar()