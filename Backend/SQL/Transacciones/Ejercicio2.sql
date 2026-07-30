DO $$
DECLARE
    v_user_id INT  := 1;
    v_items   JSON := '[{"id": 1, "qty": 1}, {"id": 5, "qty": 2}]'; 
    v_bill_id       INT;
    v_current_stock INT;
    v_product_name  VARCHAR;
    item            RECORD;
BEGIN
    IF NOT EXISTS (SELECT 1 FROM transactions.Users WHERE user_id = v_user_id) THEN
        RAISE EXCEPTION 'Transacción cancelada: el usuario con ID % no existe.', v_user_id;
    END IF;
 
    CREATE TEMP TABLE tmp_items ON COMMIT DROP AS
    SELECT id AS product_id, SUM(qty)::INT AS qty
    FROM json_populate_recordset(null::record, v_items) AS (id INT, qty INT)
    GROUP BY id;
 
    IF NOT EXISTS (SELECT 1 FROM tmp_items) THEN
        RAISE EXCEPTION 'Transacción cancelada: no se recibió ningún producto.';
    END IF;
 
    IF EXISTS (SELECT 1 FROM tmp_items WHERE qty IS NULL OR qty <= 0) THEN
        RAISE EXCEPTION 'Transacción cancelada: las cantidades deben ser mayores a cero.';
    END IF;
 
    FOR item IN SELECT product_id, qty FROM tmp_items ORDER BY product_id
    LOOP
        SELECT name, stock
          INTO v_product_name, v_current_stock
        FROM transactions.Products
        WHERE product_id = item.product_id
        FOR UPDATE;
 
        IF NOT FOUND THEN
            RAISE EXCEPTION 'Transacción cancelada: el producto ID % no existe.', item.product_id;
        END IF;
 
        IF v_current_stock < item.qty THEN
            RAISE EXCEPTION 'Transacción cancelada: stock insuficiente para "%" (ID %). Disponible: %, solicitado: %.',
                v_product_name, item.product_id, v_current_stock, item.qty;
        END IF;
    END LOOP;
 
    INSERT INTO transactions.Bills (user_id, status)
    VALUES (v_user_id, 'Completada')
    RETURNING bill_id INTO v_bill_id;
 
    INSERT INTO transactions.Bill_Details (bill_id, product_id, quantity)
    SELECT v_bill_id, product_id, qty FROM tmp_items;
 
    UPDATE transactions.Products p
    SET stock = p.stock - t.qty
    FROM tmp_items t
    WHERE p.product_id = t.product_id;
 
    RAISE NOTICE 'Compra registrada correctamente. Factura ID: %', v_bill_id;
END;
$$;