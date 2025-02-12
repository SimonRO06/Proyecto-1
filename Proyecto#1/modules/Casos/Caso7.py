import json
from modules.ControlPantalla import limpiar_pantalla, pausar
from modules.Diccionarios import libros,peliculas,musicas,IdentificadorUnico
def caso7(menu):
    limpiar_pantalla()
    data = {
    "libros": libros,
    "peliculas": peliculas,
    "canciones": musicas,
    "identificador": IdentificadorUnico
        }
    print(menu)
    try:
        seleccion = int(input("Introduzca su elección: "))
    except ValueError:
        print("La opción no es válida.")
        pausar()
        return
    match seleccion:
        case 1:
            with open("datos.json", "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4)
                print("Datos guardados exitosamente.")
                pausar()
        case 2:
            try:
                with open("datos.json", "r", encoding="utf-8") as archivo:
                    data = json.load(archivo)
                    libros.update(data.get("libros"))
                    peliculas.update(data.get("peliculas"))
                    musicas.update(data.get("canciones"))
                    IdentificadorUnico.append(data.get("identificador"))
            except FileNotFoundError:
                print('No se encontro un archivo de colección guardado')
            else:
                print('Datos cargada exitosamente')
                pausar()
        case 3:
            pass
        case _:
            print('La opción no es válida, seleccione una del menú de opciones')
            pausar()