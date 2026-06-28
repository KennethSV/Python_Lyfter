CREATE OR REPLACE PROCEDURE transactions.process_return(
    p_bill_id INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_bill_status VARCHAR;
    detail RECORD;
BEGIN

    SELECT status INTO v_bill_status 
    FROM transactions.Bills 
    WHERE bill_id = p_bill_id FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Transacción cancelada: La factura ID % no existe.', p_bill_id;
    END IF;

    IF v_bill_status = 'Retornada' THEN
        RAISE EXCEPTION 'Transacción cancelada: La factura ID % ya fue retornada previamente.', p_bill_id;
    END IF;

    FOR detail IN SELECT product_id, quantity FROM transactions.Bill_Details WHERE bill_id = p_bill_id
    LOOP

        UPDATE transactions.Products
        SET stock = stock + detail.quantity
        WHERE product_id = detail.product_id;
    END LOOP;

    UPDATE transactions.Bills
    SET status = 'Retornada'
    WHERE bill_id = p_bill_id;
END;
$$;