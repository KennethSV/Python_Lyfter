'''
5. Exportar todos los datos actuales a un archivo CSV.
6. Importar los datos de un archivo CSV previamente exportado.
'''

import csv

def escribir_archivo_csv(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)

def importar_archivo_csv(file_path):
    def try_convert(value):
        try:
            return int(value)
        except ValueError:
            return value 
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
            archivo_importado = csv.DictReader(file)
            contenido_archivo = [{key: try_convert(value) for key, value in row.items()} for row in archivo_importado]
    return contenido_archivo