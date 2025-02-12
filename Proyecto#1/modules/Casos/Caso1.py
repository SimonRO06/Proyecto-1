from modules.ControlPantalla import limpiar_pantalla,pausar
import modules.Menus as Menus
from modules.Diccionarios import libros,peliculas,musicas
from modules.Diccionarios  import IdentificadorUnico
# Añadir un Nuevo Elemento:
def caso1(menu):
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
                limpiar_pantalla()
                while True:
                    name = input('Ingrese el titulo del libro: ')
                    if name.replace(' ','').isalnum():
                            break
                    else:
                        print('El nombre del libro no puede estar vacio, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    authorName = input('Ingrese el nombre del autor: ')
                    if authorName.replace(' ','').isalpha():
                        break
                    else:
                        print('El nombre del autor no puede contener numeros, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    gender = input('Ingrese el genero del libro: ')
                    if gender.replace(' ', '').isalpha():
                        break
                    else:
                        print('El genero no puede contener numeros, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    id = input('Ingrese el identificador unico del libro: ')
                    if id in IdentificadorUnico:
                        print('El identificador debe ser unico')
                        pausar()
                    else:
                        IdentificadorUnico.append(id)
                        break
                while True:
                    try:
                        assesment = float(input('Ingrese la valoracion que le da a la musica (1.0 - 5.0): '))
                    except ValueError:
                        print('La valoracion solo puede contener numeros...')
                        pausar()
                    else:
                        if assesment < 1.0 or assesment > 5.0:
                                print('La valoracion solo puede ir de 1.0 a 5.0')
                                pausar()
                        else:
                            break
                libro = {
                    "Nombre": name,
                    "Autor": authorName,
                    "Genero": gender,
                    "ID": id.replace(' ',''),
                    "Valoracion": assesment
                    }
                libros.update({len(libros):libro})
                print(f'El libro guardado fue: {name}')
                pausar()
            case 2:
                limpiar_pantalla()
                while True:
                    name = input('Ingrese el titulo de la pelicula: ')
                    if name.replace(' ','').isalnum():
                            break
                    else:
                        print('El nombre de la pelicula no puede estar vacio, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    authorName = input('Ingrese el nombre del director: ')
                    if authorName.replace(' ','').isalpha():
                        break
                    else:
                        print('El nombre del director no puede contener numeros, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    gender = input('Ingrese el genero de la pelicula: ')
                    if gender.replace(' ', '').isalpha():
                        break
                    else:
                        print('El genero no puede contener numeros, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    id = input('Ingrese el identificador unico del libro: ')
                    if id in IdentificadorUnico:
                        print('El identificador debe ser unico')
                        pausar()
                    else:
                        IdentificadorUnico.append(id)
                        break
                while True:
                    try:
                        assesment = float(input('Ingrese la valoracion que le da a la musica (1.0 - 5.0): '))
                    except ValueError:
                        print('La valoracion solo puede contener numeros...')
                        pausar()
                    else:
                        if assesment < 1.0 or assesment > 5.0:
                                print('La valoracion solo puede ir de 1.0 a 5.0')
                                pausar()
                        else:
                            break
                pelicula = {
                    "Nombre": name,
                    "Autor": authorName,
                    "Genero": gender,
                    "ID": id.replace(' ',''),
                    "Valoracion": assesment
                    }
                peliculas.update({len(peliculas)+1:pelicula})
                print(f'La pelicula guardada fue: {name}')
                pausar()
            case 3:
                limpiar_pantalla()
                while True:
                    name = input('Ingrese el titulo de la musica: ')
                    if name.replace(' ','').isalnum():
                            break
                    else:
                        print('El nombre de la musica no puede estar vacio, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    authorName = input('Ingrese el nombre del artista: ')
                    if authorName.replace(' ','').isalpha():
                        break
                    else:
                        print('El nombre del artista no puede contener numeros, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    gender = input('Ingrese el genero de la musica: ')
                    if gender.replace(' ', '').isalpha():
                        break
                    else:
                        print('El genero no puede contener numeros, porfavor ingrese uno valido...')
                        pausar()
                while True:
                    id = input('Ingrese el identificador unico del libro: ')
                    if id in IdentificadorUnico:
                        print('El identificador debe ser unico')
                        pausar()
                    else:
                        IdentificadorUnico.append(id)
                        break
                while True:
                    try:
                        assesment = float(input('Ingrese la valoracion que le da a la musica (1.0 - 5.0): '))
                    except ValueError:
                        print('La valoracion solo puede contener numeros...')
                        pausar()
                    else:
                        if assesment < 1.0 or assesment > 5.0:
                                print('La valoracion solo puede ir de 1.0 a 5.0')
                                pausar()
                        else:
                            break
                musica = {
                    "Nombre": name,
                    "Autor": authorName,
                    "Genero": gender,
                    "ID": id.replace(' ',''),
                    "Valoracion": assesment
                    }
                musicas.update({len(musicas)+1:musica})
                print(f'La musica guardada fue: {name}')
                pausar()
            case 4:
                pass
            case _:
                print('La opcion no es valida, seleccione una del menu de opciones')
                pausar()