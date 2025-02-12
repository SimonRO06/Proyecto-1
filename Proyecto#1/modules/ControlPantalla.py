from os import system
import sys
def limpiar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def pausar():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("Presione un tecla para continuar...")
  else:
    system("pause")