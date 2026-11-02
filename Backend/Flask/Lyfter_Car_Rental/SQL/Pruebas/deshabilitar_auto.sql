-- PostgreSQL
-- Tarea 2: Deshabilitar un automovil del alquiler
-- Solo se deshabilita si no tiene un alquiler activo

UPDATE lyfter_car_rental.Automoviles
SET estado = 'Deshabilitado'
WHERE automovil_id = 3
  AND estado <> 'Alquilado'
RETURNING automovil_id, marca, modelo, estado;
