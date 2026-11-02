-- PostgreSQL
-- Tarea 2: Agregar un usuario nuevo

INSERT INTO lyfter_car_rental.Usuarios (nombre, correo, username, password, fecha_nacimiento)
VALUES ('Kenneth Solorzano Valverde', 'kenneth.solorzano@lyfter.com', 'kenneth.solorzano', crypt('Cisco123!', gen_salt('bf')), '1990-06-18')
RETURNING usuario_id, nombre, username, estado;
