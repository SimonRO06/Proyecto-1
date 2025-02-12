from modules.ControlPantalla import limpiar_pantalla,pausar
import modules.Menus as Menus
from modules.Diccionarios import libros,peliculas,musicas
def caso2(menu):
    limpiar_pantalla()
    print(menu)
    try:
        seleccion = int(input('Introduzca su eleccion: '))
    except ValueError:
        print('La opcion no es valida')
        pausar()
    else:
        match seleccion:
            case 1:
                print(f'Estos son todos los libros: {libros}')
                pausar()
            case 2:
                print(f'Estas son todas las peliculas: {peliculas}')
                pausar()
            case 3:
                print(f'Estas son todas las musicas: {musicas}')
                pausar()
            case 4:
                pass
            case _:
                print('La opcion no es valida, seleccione una del menu de opciones')
                pausar()