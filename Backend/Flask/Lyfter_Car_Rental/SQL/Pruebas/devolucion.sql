-- PostgreSQL
-- Tarea 2: Confirmar la devolucion del auto al completar el alquiler
-- El auto vuelve a quedar 'Disponible' y el alquiler pasa a 'Completado'

DO $$
DECLARE
    v_alquiler_id     INT := 12;
    v_alquiler_estado VARCHAR;
    v_automovil_id    INT;
BEGIN
    SELECT estado, automovil_id
      INTO v_alquiler_estado, v_automovil_id
    FROM lyfter_car_rental.Alquileres
    WHERE alquiler_id = v_alquiler_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Transacción cancelada: el alquiler ID % no existe.', v_alquiler_id;
    END IF;

    IF v_alquiler_estado <> 'Activo' THEN
        RAISE EXCEPTION 'Transacción cancelada: el alquiler ID % no está activo (estado: %).',
            v_alquiler_id, v_alquiler_estado;
    END IF;

    UPDATE lyfter_car_rental.Alquileres
    SET estado = 'Completado',
        fecha_devolucion = CURRENT_TIMESTAMP
    WHERE alquiler_id = v_alquiler_id;

    UPDATE lyfter_car_rental.Automoviles
    SET estado = 'Disponible'
    WHERE automovil_id = v_automovil_id;

    RAISE NOTICE 'Devolución procesada. Alquiler ID % completado, automóvil ID % disponible.',
        v_alquiler_id, v_automovil_id;
END;
$$;
