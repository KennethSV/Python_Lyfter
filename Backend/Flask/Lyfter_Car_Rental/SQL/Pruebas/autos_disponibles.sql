-- PostgreSQL
-- Tarea 2: Obtener todos los automoviles disponibles

SELECT automovil_id, marca, modelo, anio_fabricacion, estado
FROM lyfter_car_rental.Automoviles
WHERE estado = 'Disponible'
ORDER BY automovil_id;
