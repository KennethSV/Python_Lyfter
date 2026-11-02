-- PostgreSQL
-- Tarea 2: Cambiar el estado de un automovil
-- No se modifica un auto que este alquilado, primero se debe completar el alquiler

UPDATE lyfter_car_rental.Automoviles
SET estado = 'Mantenimiento'
WHERE automovil_id = 1
  AND estado <> 'Alquilado'
RETURNING automovil_id, marca, modelo, estado;
