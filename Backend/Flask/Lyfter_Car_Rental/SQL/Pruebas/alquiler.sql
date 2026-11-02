-- PostgreSQL
-- Tarea 2: Generar un alquiler nuevo con los datos de un usuario y un automovil

DO $$
DECLARE
    v_usuario_id    INT := 2;
    v_automovil_id  INT := 2;
    v_usuario_estado VARCHAR;
    v_usuario_moroso BOOLEAN;
    v_auto_estado    VARCHAR;
    v_alquiler_id    INT;
BEGIN
    SELECT estado, moroso
      INTO v_usuario_estado, v_usuario_moroso
    FROM lyfter_car_rental.Usuarios
    WHERE usuario_id = v_usuario_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Transacción cancelada: el usuario con ID % no existe.', v_usuario_id;
    END IF;

    IF v_usuario_estado <> 'Activo' THEN
        RAISE EXCEPTION 'Transacción cancelada: el usuario con ID % no está activo.', v_usuario_id;
    END IF;

    IF v_usuario_moroso THEN
        RAISE EXCEPTION 'Transacción cancelada: el usuario con ID % está marcado como moroso.', v_usuario_id;
    END IF;

    SELECT estado
      INTO v_auto_estado
    FROM lyfter_car_rental.Automoviles
    WHERE automovil_id = v_automovil_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Transacción cancelada: el automóvil con ID % no existe.', v_automovil_id;
    END IF;

    IF v_auto_estado <> 'Disponible' THEN
        RAISE EXCEPTION 'Transacción cancelada: el automóvil con ID % no está disponible (estado: %).',
            v_automovil_id, v_auto_estado;
    END IF;

    INSERT INTO lyfter_car_rental.Alquileres (usuario_id, automovil_id)
    VALUES (v_usuario_id, v_automovil_id)
    RETURNING alquiler_id INTO v_alquiler_id;

    UPDATE lyfter_car_rental.Automoviles
    SET estado = 'Alquilado'
    WHERE automovil_id = v_automovil_id;

    RAISE NOTICE 'Alquiler ID % creado: usuario % - automóvil %.',
        v_alquiler_id, v_usuario_id, v_automovil_id;
END;
$$;
