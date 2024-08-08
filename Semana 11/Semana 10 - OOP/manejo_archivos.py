'''
5. Exportar todos los datos actuales a un archivo CSV.
6. Importar los datos de un archivo CSV previamente exportado.
'''

import csv
import manejo_informacion

def escribir_archivo_csv(file_path, estudiantes):
  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    headers = ['Nombre completo', 'Sección', 'Nota de español', 'Nota de inglés', 'Nota de sociales', 'Nota de ciencias']
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    for estudiante in estudiantes:
        writer.writerow({
            'Nombre completo': estudiante.nombre,
            'Sección': estudiante.seccion,
            'Nota de español': estudiante.espanol,
            'Nota de inglés': estudiante.ingles,
            'Nota de sociales': estudiante.sociales,
            'Nota de ciencias': estudiante.ciencias,
        })

def importar_archivo_csv(file_path):
    manejo_informacion.lista_estudiantes = []
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            estudiante = manejo_informacion.Estudiante(
                nombre=row['Nombre completo'],
                seccion=row['Sección'],
                espanol=int(row['Nota de español']),
                ingles=int(row['Nota de inglés']),
                sociales=int(row['Nota de sociales']),
                ciencias=int(row['Nota de ciencias'])
            )
            manejo_informacion.lista_estudiantes.append(estudiante)
    return manejo_informacion.lista_estudiantes