import PySimpleGUI as sg

def restar_a_contador(contador, window):
    contador -= 1
    window['contador'].update(contador)
    return contador

def sumar_a_contador(contador, window):
    contador += 1
    window['contador'].update(contador)
    return contador

def show_main_window():
    layout = [
        [sg.Text("Felicidades por crear una GUI")],
        [sg.Button("Aceptar")],
        [sg.Button("Sumador")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Ventana Principal", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cerrar":
            break
        elif event == "Aceptar":
            show_secondary_window()
        elif event == "Sumador":
            show_contador_window()

    window.close()

def show_secondary_window():
    layout = [
        [sg.Text("Gracias por aceptar")],
        [sg.Button("Cerrar")],
    ]

    window = sg.Window("Segunda Ventana", layout)

    while True:
        event, values = window.read()

        if event == "Cerrar":
            window.close()
        elif event == sg.WIN_CLOSED:
            break
    window.close()

def show_contador_window():
    contador = 0

    layout = [
        [sg.Text("Gracias por ingresar al contador!")],
        [sg.Button("Sumar")],
        [sg.Button("Restar")],
        [sg.Button("Cerrar")],
        [sg.Text(contador, key="contador")],
    ]

    window = sg.Window("Contador", layout)

    while True:
        event, values = window.read()
        
        if event == "Cerrar":
            window.close()
        elif event == sg.WIN_CLOSED:
            break
        elif event == "Sumar":
            contador = sumar_a_contador(contador, window)
        elif event == "Restar":
            contador = restar_a_contador(contador, window)
            
    window.close()


if __name__ == "__main__":
    show_main_window()