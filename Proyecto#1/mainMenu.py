# Mi compañero es Juan Camilo Amezquita
import modules.Menus as Menus
from modules.ControlPantalla import limpiar_pantalla, pausar
import modules.FuncionMenuPrincipal as FuncionMenuPrincipal
if __name__ == "__main__":
    while True:
        limpiar_pantalla()
        print(Menus.menu_principal)
        try:
            seleccion = int(input('Introduzca su eleccion: '))
        except ValueError:
            print('La opcion no es valida')
            pausar()
        else:
            FuncionMenuPrincipal.opciones_menu_principal(seleccion)
