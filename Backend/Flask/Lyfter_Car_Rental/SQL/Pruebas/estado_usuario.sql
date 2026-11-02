-- PostgreSQL
-- Tarea 2: Cambiar el estado de un usuario

UPDATE lyfter_car_rental.Usuarios
SET estado = 'Inactivo'
WHERE usuario_id = 1
RETURNING usuario_id, username, estado;
