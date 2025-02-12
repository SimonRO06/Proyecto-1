from modules.ControlPantalla import limpiar_pantalla, pausar
import modules.Menus as Menus
from modules.Diccionarios import libros, peliculas, musicas, IdentificadorUnico

def caso5(menu):
    limpiar_pantalla()
    print(menu)
    try:
        seleccion = int(input('Introduzca su elección: '))
    except ValueError:
        print('La opción no es válida')
        pausar()
        return
    
    match seleccion:
        case 1:
            titulo = input('Ingrese el título del elemento a eliminar: ').strip().lower()
            for categoria in [libros, peliculas, musicas]:
                for clave, valor in list(categoria.items()):
                    if valor["Nombre"].strip().lower() == titulo:
                        id_unico = valor["ID"]
                        del categoria[clave]
                        
                        if id_unico in IdentificadorUnico:
                            IdentificadorUnico.remove(id_unico)
                            print(f'El identificador unico {id_unico} tambien ha sido eliminado')

                        print(f'El elemento {titulo} ha sido eliminado correctamente')
                        print('Lista actualizada de identificadores únicos:', IdentificadorUnico)
                        pausar()
                        return
            print('No se encontro ningun elemento con ese titulo')
            pausar()

        case 2:
            id_unico = input('Ingrese el ID unico del elemento a eliminar: ').strip()
            for categoria in [libros, peliculas, musicas]:
                for clave, valor in list(categoria.items()):
                    if valor["ID"] == id_unico:
                        del categoria[clave]
                        
                        if id_unico in IdentificadorUnico:
                            IdentificadorUnico.remove(id_unico)
                            print(f'El identificador unico {id_unico} tambien ha sido eliminado')

                        print(f'El elemento con ID: {id_unico} ha sido eliminado correctamente')
                        print("Lista actualizada de identificadores unicos:", IdentificadorUnico)
                        pausar()
                        return
            print('No se encontro ningun elemento con ese ID')
            pausar()
        case 3:
            pass
        case _:
            print('La opción no es válida')
            pausar()
            return
