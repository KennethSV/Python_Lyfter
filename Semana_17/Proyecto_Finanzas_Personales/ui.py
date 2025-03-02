'''
# Requerimientos

Investigue sobre la biblioteca [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) 
y cree un programa **con interfaz gráfica** que permita la gestión de finanzas 
personales. Este debe mostrar:

- Una tabla de movimientos (gastos e ingresos).
- Un botón para agregar una categoría de movimiento.
    - Este botón debe abrir otra ventana para agregar esa categoría.
    - Por ejemplo: Comida, Familia, Carro, etc.
- Un botón para agregar un gasto.
    - Este botón debe abrir otra ventana para agregar ese gasto.
    - Los gastos deben tener un titulo, un monto y una categoría.
- Un botón para agregar un ingreso.
    - Este botón debe abrir otra ventana para agregar esa ingreso.
    - Los ingresos deben tener un titulo, un monto y una categoría.

Así mismo:

- Si yo intento agregar un ingreso o un gasto, pero no hay  ninguna categoría 
agregada previamente, debe mostrar un error que diga 
“Por favor ingrese una categoría antes”.
- Cada vez que haga cambios, se debe exportar la data automáticamente en archivos.
- Cada vez que yo abra el programa, debe importar la data automáticamente (si existe).
- Toda la lógica debe ir separada en módulos y funciones.

# Proceso de descomposición

1. Hacer mockups de cada ventana.
    1. Investigar los elementos necesarios para cada ventana.
2. Diseñar como se va a guardar la data.
    1. Qué estructura tendrán a nivel de memoria.
3. Dividir funcionamientos en tareas más pequeñas.
    1. Partes “unitarias” que se puedan probar individualmente.
4. Empezar a desarrollar paso a paso.
    1. Que cada cosa funcione antes de seguir con la siguiente.
    2. No saltar a otro paso sin tener el primero listo.
'''

import PySimpleGUI as sg
import manejo_archivo_csv
import csv

ubicacion_archivo = 'finanzas.csv'
headers = ["Categoria", "Gasto", "Ingreso"]

manejo_archivo_csv.importar_archivo_csv(ubicacion_archivo)

def mostrar_ventana_principal():
    layout = [
        [sg.Text("Bienvenido a sistema de finanzas\nQue acción desea realizar el día de hoy?")],
        [sg.Button("Agregar Categoría")],
        [sg.Button("Agregar Gasto")],
        [sg.Button("Agregar Ingreso")],
        [sg.Button("Ver Tabla de Movimientos")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Sistema Finanzas", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar":
            break
        elif event == "Agregar Categoría":
            agregar_categoria()
        elif event == "Agregar Gasto":
            agregar_gasto()
        elif event == "Agregar Ingreso":
            agregar_ingreso()
        elif event == "Ver Tabla de Movimientos":
            ver_tabla_movimientos()
    window.close()

def agregar_categoria():

    layout = [
        [sg.Input(default_text='', key='Input')],
        [sg.Button("Aceptar Cambio")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Categorias", layout)

    while True:
        event, values = window.read()
        
        if event in ("Cerrar", sg.WIN_CLOSED):
            break
        
        if event == "Aceptar Cambio":
            categoria = values['Input'].strip()
            
            if categoria:  # Only add if it's not empty
                new_data = [{"Categoria": categoria}]
                manejo_archivo_csv.escribir_archivo_csv(ubicacion_archivo, new_data, headers)
                sg.popup("Categoría agregada exitosamente.", title="Éxito")
            window.close()
            break
        window.close()

def agregar_gasto():

    gasto = 0

    layout = [
        [sg.Input(default_text='', key='Input')],
        [sg.Button("Aceptar Cambio")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Gastos", layout)

    while True:
        event, values = window.read()
        if event == "Aceptar Cambio":
            categoria = window['Input'].get()
            print(categoria)
            window.close()
        if event == "Cerrar":
            window.close()
        elif event == sg.WIN_CLOSED:
            break
    window.close()

def agregar_ingreso():

    layout = [
        [sg.Input(default_text='', key='Input')],
        [sg.Button("Aceptar Cambio")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Ingresos", layout)

    while True:
        event, values = window.read()
        if event == "Aceptar Cambio":
            categoria = window['Input'].get()
            print(categoria)
            window.close()
        if event == "Cerrar":
            window.close()
        elif event == sg.WIN_CLOSED:
            break
    window.close()

def ver_tabla_movimientos():

    layout = [
        [sg.Input(default_text='', key='Input')],
        [sg.Button("Aceptar Cambio")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Movimientos", layout)

    while True:
        event, values = window.read()
        if event == "Aceptar Cambio":
            categoria = window['Input'].get()
            print(categoria)
            window.close()
        if event == "Cerrar":
            window.close()
        elif event == sg.WIN_CLOSED:
            break
    window.close()

if __name__ == "__main__":
    mostrar_ventana_principal()