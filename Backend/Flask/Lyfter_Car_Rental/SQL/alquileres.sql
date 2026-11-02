-- PostgreSQL
-- Tarea 1.4: Tabla cruz que relaciona los alquileres de los automoviles con los usuarios
-- La fecha_alquiler se genera automaticamente al ingresar una nueva fila

CREATE TABLE lyfter_car_rental.Alquileres (
    alquiler_id      SERIAL PRIMARY KEY,
    usuario_id       INT NOT NULL,
    automovil_id     INT NOT NULL,
    fecha_alquiler   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_devolucion TIMESTAMP,
    estado           VARCHAR(20) NOT NULL DEFAULT 'Activo'
    CHECK (estado IN ('Activo', 'Completado', 'Cancelado')),
    FOREIGN KEY (usuario_id)   REFERENCES lyfter_car_rental.Usuarios(usuario_id),
    FOREIGN KEY (automovil_id) REFERENCES lyfter_car_rental.Automoviles(automovil_id)
);

-- Historial de alquileres ya cerrados (con fecha explicita en el pasado)
INSERT INTO lyfter_car_rental.Alquileres (usuario_id, automovil_id, fecha_alquiler, fecha_devolucion, estado) VALUES
(1, 1, '2026-01-01 09:00:00', '2026-01-01 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(2, 2, '2026-02-04 09:00:00', '2026-02-04 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(4, 3, '2026-03-07 09:00:00', '2026-03-07 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(5, 4, '2026-04-10 09:00:00', '2026-04-10 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(6, 5, '2026-05-13 09:00:00', '2026-05-13 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(7, 8, '2026-06-16 09:00:00', '2026-06-16 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(8, 9, '2026-07-19 09:00:00', '2026-07-19 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(9, 10, '2026-08-22 09:00:00', '2026-08-22 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(10, 11, '2026-09-25 09:00:00', '2026-09-25 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(11, 12, '2026-01-01 09:00:00', '2026-01-01 09:00:00'::TIMESTAMP + INTERVAL '3 days', 'Completado'),
(20, 23, '2026-10-05 14:30:00', NULL, 'Cancelado');

-- Alquileres activos (fecha_alquiler autogenerada)
INSERT INTO lyfter_car_rental.Alquileres (usuario_id, automovil_id) VALUES
(12, 13),
(13, 14),
(14, 15),
(15, 16),
(16, 17),
(17, 18),
(18, 21),
(19, 22);

-- Los automoviles con un alquiler activo quedan como 'Alquilado'
UPDATE lyfter_car_rental.Automoviles
SET estado = 'Alquilado'
WHERE automovil_id IN (
    SELECT automovil_id
    FROM lyfter_car_rental.Alquileres
    WHERE estado = 'Activo'
);
