import sys
import pprint
import manejo_informacion
import manejo_archivos

ubicacion_archivo = 'estudiantes.csv'
keys = ['Nombre completo', 'Sección', 'Nota de español', 'Nota de inglés', 'Nota de sociales', 'Nota de ciencias']

def desplegar_menu():
    menu = 0
    try:
        menu = int(input(f"Bienvenido al sistema de control de estudiantes\nDigite uno de los siguientes valores según su preferencia:\n1. Ingresar información de n cantidad de estudiantes, uno por uno.\n2. Ver la información de todos los estudiantes ingresados.\n3. Ver el top 3 de los estudiantes con la mejor nota promedio\n4. Ver la nota promedio entre las notas de todos los estudiantes\n5. Exportar todos los datos actuales a un archivo CSV.\n6. Importar los datos de un archivo CSV previamente exportado.\n7. Salir\nDigite una de las opciones del menú: "))
        if menu < 1 or menu > 7:
            raise ValueError("Numero no está dentro de la lista")
    except ValueError as error:
        print(f"El dato ingresado no corresponde a un número dentro del menú, debido a: {error}")
    if menu == 1:
        manejo_informacion.ingresar_estudiante()
        manejo_informacion.calcular_promedios()
        manejo_informacion.calcular_top3()
        desplegar_menu()
    elif menu == 2:
        if not manejo_informacion.lista_estudiantes:
            print("Actualmente la tabla de estudiantes está vacía, favor ingresar datos\n")
        else:
            pprint.pprint(manejo_informacion.lista_estudiantes)
        desplegar_menu()
    elif menu == 3:
        if not manejo_informacion.lista_top3:
            print("Actualmente la tabla de estudiantes está vacía, favor ingresar datos\n")
        else:
            pprint.pprint(manejo_informacion.lista_top3)
        desplegar_menu()
    elif menu == 4:
        if not manejo_informacion.lista_promedios:
            print("Actualmente la tabla de estudiantes está vacía, favor ingresar datos\n")
        else:
            pprint.pprint(manejo_informacion.lista_promedios)
        desplegar_menu()
    elif menu == 5:
        if not manejo_informacion.lista_estudiantes:
            print("Actualmente la tabla de estudiantes está vacía, favor ingresar datos\n")
        else:
            manejo_archivos.escribir_archivo_csv(ubicacion_archivo, manejo_informacion.lista_estudiantes, keys)
            print("Archivo creado!")
        desplegar_menu()
    elif menu == 6:
        try:
            manejo_informacion.lista_estudiantes = manejo_archivos.importar_archivo_csv(ubicacion_archivo)
        except Exception as error:
            print(f"Archivo no existe ver siguiente error: {error}")
        desplegar_menu()
    else:
        sys.exit()


if __name__ == '__main__':
	desplegar_menu()