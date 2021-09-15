# Importamos las funciones principales
from utilidades import funciones

# Importamos la función time para dar una mejor experiencia de usuario
import time

# Variable para guardar la información del usuario
usuario = None

# Función que ejecuta el programa
def ejecutar():
    bandera = True
    while bandera:
        opcion = input(
            "Acciones disponibles:\n - Registro\n - Login\n").replace(
                " ", "").lower()
        if opcion == "registro":
            funciones.registro()
            time.sleep(2)
            continue
        elif opcion == "login":
            usuario = funciones.login()
            if usuario:
                bandera = False
        else:
            print("Tu opción no ha sido encontrada")
    bandera = True
    while bandera:
        print('eliga un numero:')
        print('   1. Crear nota  \n   2. Mostrar Notas  \n   3. Eliminar nota  \n   4. Salir ')
        opcion = input('opcion: ')
        if opcion == "1":
            funciones.crearNota(usuario)
        elif opcion == "2":
            funciones.listarNotas(usuario)
        elif opcion == "3":
            funciones.eliminarNota(usuario)
        elif opcion == "4":
            bandera = False
        else:
            print("Tu opción no ha sido encontrada")
# TODO
# Validación de emailTODO

# Ejecutamos como archivo principal
if __name__ == "__main__":
    ejecutar() 