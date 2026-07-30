DO $$
DECLARE
    v_bill_id INT := 1;
    v_bill_status VARCHAR;
    v_lineas      INT;
    detail        RECORD;
BEGIN
    SELECT status
      INTO v_bill_status
    FROM transactions.Bills
    WHERE bill_id = v_bill_id
    FOR UPDATE;
 
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Transacción cancelada: la factura ID % no existe.', v_bill_id;
    END IF;
 
    IF v_bill_status = 'Retornada' THEN
        RAISE EXCEPTION 'Transacción cancelada: la factura ID % ya fue retornada previamente.', v_bill_id;
    END IF;
 
    FOR detail IN
        SELECT product_id, quantity
        FROM transactions.Bill_Details
        WHERE bill_id = v_bill_id
        ORDER BY product_id
    LOOP
        UPDATE transactions.Products
        SET stock = stock + detail.quantity
        WHERE product_id = detail.product_id;
    END LOOP;
 
    UPDATE transactions.Bills
    SET status = 'Retornada'
    WHERE bill_id = v_bill_id;
 
    SELECT COUNT(*) INTO v_lineas
    FROM transactions.Bill_Details
    WHERE bill_id = v_bill_id;
 
    RAISE NOTICE 'Devolución procesada. Factura ID %: % línea(s) reintegrada(s) al stock.',
        v_bill_id, v_lineas;
END;
$$;