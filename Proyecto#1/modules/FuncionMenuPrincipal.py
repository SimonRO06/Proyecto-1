from modules.ControlPantalla import limpiar_pantalla, pausar
import modules.Menus as Menus
from modules.Casos.Caso1 import caso1
from modules.Casos.Caso2 import caso2
from modules.Casos.Caso3 import caso3
from modules.Casos.Caso4 import caso4
from modules.Casos.Caso5 import caso5
from modules.Casos.Caso6 import caso6
from modules.Casos.Caso7 import caso7
from modules.Diccionarios import libros,peliculas,musicas
import json
import modules.Diccionarios as d
def opciones_menu_principal(seleccion):
    while True:
        match seleccion:
            case 1:
                caso1(Menus.menu_opciones_nuevo_elemento)
                break
            case 2:
                caso2(Menus.menu_opciones_ver_elementos)
                break
            case 3:
                caso3(Menus.menu_opciones_buscar_elemento)
                break
            case 4:
                caso4(Menus.menu_opciones_editar_elemento,Menus.menu_tipo_elemento)
                break
            case 5:
                caso5(Menus.menu_opciones_eliminar_elemento)
                break
            case 6:
                caso6(Menus.menu_opciones_ver_elemento_categoria)
                break
            case 7:
                caso7(Menus.menu_opciones_guardar_cargar_coleccion)
                break
            case 8:
                print('Cerrando programa...')
                break
            case _:
                print('La opcion no es valida, seleccione una del menu de opciones')
                pausar()
                break
#Este es el menu principal que contiene cada uno de los menus y las opciones que tiene.