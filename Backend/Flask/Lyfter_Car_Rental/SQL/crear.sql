-- PostgreSQL
-- Tarea 1.1: Crear el schema donde se trabajan todos los ejercicios

CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;

-- Extension usada para guardar los passwords encriptados (crypt / gen_salt)
CREATE EXTENSION IF NOT EXISTS pgcrypto;
