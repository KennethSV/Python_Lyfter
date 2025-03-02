import csv
import os

def escribir_archivo_csv(file_path, new_data, headers):
    existing_data = []
    if os.path.exists(file_path):
        existing_data = importar_archivo_csv(file_path)
    existing_keys = {tuple(item.values()) for item in existing_data}
    updated_data = existing_data + [row for row in new_data if tuple(row.values()) not in existing_keys]

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_data)

def importar_archivo_csv(file_path):
    def try_convert(value):
        try:
            return int(value)
        except ValueError:
            return value 

    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        archivo_importado = csv.DictReader(file)
        contenido_archivo = [{key: try_convert(value) for key, value in row.items()} for row in archivo_importado]

    return contenido_archivo
