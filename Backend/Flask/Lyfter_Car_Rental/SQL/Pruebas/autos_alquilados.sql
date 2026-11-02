-- PostgreSQL
-- Tarea 2: Obtener todos los automoviles alquilados (con el usuario que lo tiene)

SELECT a.automovil_id, a.marca, a.modelo, a.anio_fabricacion,
       al.alquiler_id, al.fecha_alquiler,
       u.usuario_id, u.nombre, u.username
FROM lyfter_car_rental.Automoviles a
JOIN lyfter_car_rental.Alquileres al ON al.automovil_id = a.automovil_id AND al.estado = 'Activo'
JOIN lyfter_car_rental.Usuarios u    ON u.usuario_id = al.usuario_id
WHERE a.estado = 'Alquilado'
ORDER BY a.automovil_id;
