-- PostgreSQL
-- Tarea 2: Agregar un automovil nuevo

INSERT INTO lyfter_car_rental.Automoviles (marca, modelo, anio_fabricacion)
VALUES ('Toyota', 'Corolla Cross', 2025)
RETURNING automovil_id, marca, modelo, anio_fabricacion, estado;
