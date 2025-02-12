from modules.ControlPantalla import limpiar_pantalla,pausar
import modules.Menus as Menus
from modules.Diccionarios import libros,peliculas,musicas

def caso4(menu,menu_tipo_elemento):
    limpiar_pantalla()
    print(menu)
    try:
        seleccion = int(input('Introduzca su elección: '))
    except ValueError:
        print('La opción no es válida')
        pausar()
        return
    coleccion = {1: libros, 2: peliculas, 3: musicas}
    print(menu_tipo_elemento)
    try:
        categoria = int(input("Ingrese el número de la categoría: "))
    except ValueError:
        print('La opción no es válida')
        pausar()
        return
    else:
        if categoria not in coleccion:
            print('Categoria no valida')
            pausar()
            return
        diccionario = coleccion[categoria]
        if not diccionario:
            print('No hay elementos en esta categoria')
            pausar()
            return
        identificador = input('Ingrese el ID del elemento que desea editar: ')
        elemento = next((v for k, v in diccionario.items() if v["ID"] == identificador), None)
        if not elemento:
            print('No se encontro un elemento con ese ID')
            pausar()
            return
        match seleccion:
            case 1:
                nuevo_titulo = input('Ingrese el nuevo título: ')
                elemento["Nombre"] = nuevo_titulo
            case 2:
                nuevo_autor = input('Ingrese el nuevo Autor/Director/Artista: ')
                if nuevo_autor.replace(' ', '').isalpha():
                    elemento["Autor"] = nuevo_autor
                else:
                    print('El nombre no puede contener numeros')
                    pausar()
                    return
            case 3:
                nuevo_genero = input("Ingrese el nuevo genero: ")
                if nuevo_genero.replace(' ', '').isalpha():
                    elemento["Genero"] = nuevo_genero
                else:
                    print('El genero no puede contener numeros')
                    pausar()
                    return
            case 4:
                try:
                    nueva_valoracion = float(input('Ingrese la nueva valoracion (1.0 - 5.0): '))
                    if nueva_valoracion >= 1.0 or nueva_valoracion <= 5.0:
                        elemento["Valoracion"] = nueva_valoracion
                    else:
                        print('La valoracion debe estar entre 1.0 y 5.0')
                        pausar()
                        return
                except ValueError:
                    print('La valoracion solo puede contener números')
                    pausar()
                    return
            case 5:
                pass
            case _:
                print('La opción no es válida')
                pausar()
                return



