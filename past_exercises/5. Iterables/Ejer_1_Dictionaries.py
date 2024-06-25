"""Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones
El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
numero
piso
precio_por_noche"""

dict_hotel = [
    {
    "nombre": "Hilton",
    "numero de estrellas": 3,
    "habitaciones": [
        {
            "numero:": 1,
            "piso": 1, 
            "precio_por_noche": 300
        },
        {
            "numero:": 2,
            "piso": 1, 
            "precio_por_noche": 300
        },
        {
            "numero:": 3,
            "piso": 1, 
            "precio_por_noche": 300
        },
    ]
    },
    {
    "nombre": "Park Inn",
    "numero de estrellas": 2,
    "habitaciones": [
        {
            "numero:": 4,
            "piso": 2, 
            "precio_por_noche": 200
        },
        {
            "numero:": 5,
            "piso": 2, 
            "precio_por_noche": 250
        },
        {
            "numero:": 6,
            "piso": 3, 
            "precio_por_noche": 400
        },
    ]
    },
]

print(dict_hotel[1]["habitaciones"][0]["precio_por_noche"])