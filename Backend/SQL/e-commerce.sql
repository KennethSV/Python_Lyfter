-- SQLite

CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre_completo_usuario VARCHAR,
    correo VARCHAR,
    fecha_registro TEXT
);

CREATE TABLE metodos_de_pago (
    id INT PRIMARY KEY,
    tipo VARCHAR,
    nombre_banco varchar
);


CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre TEXT,
    precio FLOAT,
    fecha_ingreso TEXT,
    marca TEXT
);

CREATE TABLE carrito_compras (
    id INT PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id)
);

CREATE TABLE resenas (
    id INT PRIMARY KEY,
    producto_id INT REFERENCES productos(id),
    usuario_id INT REFERENCES usuarios(id),
    comentario VARCHAR,
    calification INT,
    fecha_resena TEXT
);

CREATE TABLE facturas (
    id INT PRIMARY KEY,
    metodos_de_pago_id INT REFERENCES metodos_de_pago(id),
    usuario_id INT REFERENCES usuarios(id),
    fecha_compra TEXT
);

CREATE TABLE factura_producto (
    id INT PRIMARY KEY,
    numero_factura_id INT REFERENCES facturas(id),
    producto_id INT REFERENCES productos(id),
    cantidad_comprada INT,
    monto_total FLOAT
);


CREATE TABLE producto_carrito_compras (
    id INT PRIMARY KEY,
    producto_id INT REFERENCES productos(id),
    carrito_compras_id INT REFERENCES carrito_compras(id)
);

# 3. Modifique la tabla de Facturas creada en el ejercicio anterior y agregue una columna para almacenar también 
# el número de teléfono del comprador, y otra para el código de empleado del cajero que realizó la venta.

ALTER TABLE facturas ADD COLUMN usuario_telefono int NOT NULL CHECK (usuario_telefono >= 10000000 AND usuario_telefono <= 99999999 );
ALTER TABLE facturas ADD COLUMN codigo_empleado int VARCHAR;

# Aprendí que los '' commands se deben de enviar por separados, y no requieren de estar entre parentesís'

# 4. Realice los siguientes 

# 1. Obtenga todos los productos almacenados

INSERT INTO productos (id, nombre, precio, fecha_ingreso, marca)
    VALUES(1, "Switch", 400, "12 de Marzo, 2026", "Nintendo");

INSERT INTO productos (id, nombre, precio, fecha_ingreso, marca)
    VALUES(2, "Tablet", 1000, "01 de Marzo, 2026", "Apple, Inc");

INSERT INTO productos (id, nombre, precio, fecha_ingreso, marca)
    VALUES(3, "Teclado", 300, "01 de Febrero, 2026", "Logitech");

INSERT INTO productos (id, nombre, precio, fecha_ingreso, marca)
    VALUES(4, "Mouse", 100, "01 de Febrero, 2026", "Logitech");

SELECT * from productos;

# 2. Obtenga todos los productos que tengan un precio mayor a 50000

UPDATE productos SET 
    precio = 52000
    WHERE nombre = "Tablet";

SELECT * from productos WHERE PRECIO > 50000;

# 3. Obtenga todas las compras de un mismo producto por id.

INSERT INTO usuarios (id, nombre_completo_usuario, correo, fecha_registro)
    VALUES(1, "Daniela Jimenez Solano", "djs@gmail.com", "01 de Enero, 2026");

INSERT INTO usuarios (id, nombre_completo_usuario, correo, fecha_registro)
    VALUES(2, "Kenneth Solorzano Valverde", "ksv@gmail.com", "01 de Enero, 2025");

INSERT INTO usuarios (id, nombre_completo_usuario, correo, fecha_registro)
    VALUES(3, "Aryery Solano Solano", "arsol@gmail.com", "01 de Febrero, 2026");

INSERT INTO carrito_compras (id, usuario_id)
    VALUES(1, 1);

INSERT INTO carrito_compras (id, usuario_id)
    VALUES(2, 2);

INSERT INTO carrito_compras (id, usuario_id)
    VALUES(3, 3);

INSERT INTO producto_carrito_compras (id, producto_id, carrito_compras_id)
    VALUES(1, 2, 1);

INSERT INTO producto_carrito_compras (id, producto_id, carrito_compras_id)
    VALUES(2, 1, 1);

INSERT INTO producto_carrito_compras (id, producto_id, carrito_compras_id)
    VALUES(3, 2, 2);

INSERT INTO producto_carrito_compras (id, producto_id, carrito_compras_id)
    VALUES(4, 4, 2);

SELECT * from producto_carrito_compras WHERE producto_id = 1;

# 4. Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.

INSERT INTO metodos_de_pago (id, tipo, nombre_banco) 
    VALUES (1, 'Tarjeta de Crédito', 'BAC');

INSERT INTO facturas (id, metodos_de_pago_id, usuario_id, fecha_compra, usuario_telefono, codigo_empleado) 
    VALUES (1, 1, 1, '10 de Marzo, 2026', 88881111, 'EMP01');

INSERT INTO facturas (id, metodos_de_pago_id, usuario_id, fecha_compra, usuario_telefono, codigo_empleado) 
    VALUES (2, 1, 1, '11 de Marzo, 2026', 88881111, 'EMP02');

INSERT INTO facturas (id, metodos_de_pago_id, usuario_id, fecha_compra, usuario_telefono, codigo_empleado) 
    VALUES (3, 1, 2, '12 de Marzo, 2026', 88882222, 'EMP01');

INSERT INTO factura_producto (id, numero_factura_id, producto_id, cantidad_comprada, monto_total) 
    VALUES (1, 1, 1, 2, 800.0);

INSERT INTO factura_producto (id, numero_factura_id, producto_id, cantidad_comprada, monto_total) 
    VALUES (2, 1, 4, 1, 100.0);

INSERT INTO factura_producto (id, numero_factura_id, producto_id, cantidad_comprada, monto_total) 
    VALUES (3, 2, 2, 1, 52000.0);

INSERT INTO factura_producto (id, numero_factura_id, producto_id, cantidad_comprada, monto_total) 
    VALUES (4, 3, 1, 1, 400.0);

SELECT 
    producto.nombre AS producto,
    SUM(factura_producto.cantidad_comprada) AS total_unidades,
    SUM(factura_producto.monto_total) AS total_dinero
FROM factura_producto
JOIN productos producto ON factura_producto.producto_id = producto.id
GROUP BY producto.id;

# 5. Obtenga todas las facturas realizadas por el mismo comprador

SELECT * from facturas where usuario_id = 1;

# 6. Obtenga todas las facturas ordenadas por monto total de forma descendente

SELECT 
    numero_factura_id,
    SUM(factura_producto.monto_total) AS total_dinero
FROM factura_producto
GROUP BY numero_factura_id
ORDER BY total_dinero DESC;

# 7. Obtenga una sola factura por número de factura.

SELECT * from factura_producto WHERE numero_factura_id = 2;