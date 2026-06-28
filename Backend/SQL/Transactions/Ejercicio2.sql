CREATE OR REPLACE PROCEDURE transactions.process_purchase(
    p_user_id INT,
    p_items JSON
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_user_exists BOOLEAN;
    v_bill_id INT;
    item RECORD;
    v_current_stock INT;
BEGIN
    SELECT EXISTS(SELECT 1 FROM transactions.users WHERE user_id = p_user_id) INTO v_user_exists;
    IF NOT v_user_exists THEN
        RAISE EXCEPTION 'Transacción cancelada: El usuario con ID % no existe.', p_user_id;
    END IF;

    INSERT INTO transactions.Bills (user_id, status) 
    VALUES (p_user_id, 'Completada') 
    RETURNING bill_id INTO v_bill_id;


    FOR item IN SELECT * FROM json_populate_recordset(null::record, p_items) AS (id INT, qty INT)
    LOOP

        SELECT stock INTO v_current_stock 
        FROM transactions.Products 
        WHERE product_id = item.id FOR UPDATE;

        IF NOT FOUND THEN
            RAISE EXCEPTION 'Transacción cancelada: El producto ID % no existe.', item.id;
        END IF;

        IF v_current_stock < item.qty THEN
            RAISE EXCEPTION 'Transacción cancelada: Stock insuficiente para el producto ID %.', item.id;
        END IF;

        INSERT INTO transactions.Bill_Details (bill_id, product_id, quantity)
        VALUES (v_bill_id, item.id, item.qty);

        UPDATE transactions.Products 
        SET stock = stock - item.qty 
        WHERE product_id = item.id;
    END LOOP;
END;
$$;