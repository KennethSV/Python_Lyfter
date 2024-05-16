'''
5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
    - Resolución en pseudo-código
        
        > Calcular notas
        > 
        > 1. Inicio
        > 2. Definir `total_de_notas`
        > 3. Definir `contador_de_nota`
        > 4. Definir `nota_actual`
        > 5. Definir `cantidad_de_notas_aprobadas`
        > 6. Definir `cantidad_de_notas_desaprobadas`
        > 7. Definir `promedio_de_notas_aprobadas`
        > 8. Definir `promedio_de_notas_desaprobadas`
        > 9. Definir `promedio_de_notas_total`
        > 10. `contador_de_nota` = 1
        > 11. `cantidad_de_notas_aprobadas` = 0
        > 12. `cantidad_de_notas_desaprobadas` = 0
        > 13. `promedio_de_notas_aprobadas` = 0
        > 14. `promedio_de_notas_desaprobadas` = 0
        > 15. `promedio_de_notas_total` = 0
        > 16. Mostrar “Ingrese la cantidad de notas”
        > 17. Pedir `total_de_notas`
        > 18. Mientras que (`contador_de_nota` ≤ `total_de_notas`) repetir:
        >     1. Mostrar “Ingrese la nota numero"
        >     2. Mostrar `contador_de_nota`
        >     3. Pedir `nota_actual`
        >     4. Si (`nota_actual`  < 70) entonces:
        >         1. `cantidad_de_notas_desaprobadas` =  `cantidad_de_notas_desaprobadas` + 1
        >         2. `promedio_de_notas_desaprobadas` = `promedio_de_notas_desaprobadas` + `nota_actual`
        >     5. Sino:
        >         1. `cantidad_de_notas_aprobadas` = `cantidad_de_notas_aprobadas` + 1
        >         2. `promedio_de_notas_aprobadas` = `promedio_de_notas_aprobadas` + `nota_actual`
        >     6. `promedio_de_notas_total` = `promedio_de_notas_total` + (`nota_actual` / `total_de_notas`)
        > 19. FinMientras
        > 20. `promedio_de_notas_desaprobadas` = `promedio_de_notas_desaprobadas` / `cantidad_de_notas_desaprobadas`
        > 21. `promedio_de_notas_aprobadas` = `promedio_de_notas_aprobadas` / `cantidad_de_notas_aprobadas`
        > 22. Mostrar “El estudiante tiene esta cantidad de notas aprobadas”
        > 23. Mostrar `cantidad_de_notas_aprobadas`
        > 24. Mostrar “Este es el promedio de notas aprobadas”
        > 25. Mostrar `promedio_de_notas_aprobadas`
        > 26. Mostrar “El estudiante tiene esta cantidad de notas desaprobadas”
        > 27. Mostrar `cantidad_de_notas_desaprobadas`
        > 28. Mostrar “Este es el promedio de notas desaprobadas”
        > 29. Mostrar promedio`_de_notas_desaprobadas`
        > 30. Mostrar “Este es el promedio total de notas”
        > 31. Mostrar `promedio_de_notas_total`
        > 32. Fin
'''

total_de_notas = int(input('Ingrese la cantidad de notas\n'))
contador_de_nota = 1
nota_actual = 0
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

while contador_de_nota <= total_de_notas:
    nota_actual = int(input(f'Ingrese la nota numero {contador_de_nota}\n'))
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas += 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas = nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
    promedio_de_notas_total = promedio_de_notas_total + ( nota_actual / total_de_notas )
    contador_de_nota += 1

promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas

print(f'El estudiante tiene esta cantidad de notas aprobadas: {cantidad_de_notas_aprobadas}')
print(f'Este es el promedio de notas aprobadas: {promedio_de_notas_aprobadas}')        
print(f'El estudiante tiene esta cantidad de notas desaprobadas: {cantidad_de_notas_desaprobadas}')
print(f'Este es el promedio de notas desaprobadas: {promedio_de_notas_desaprobadas}')
print(f'Este es el promedio total de notas: {promedio_de_notas_total}')