-- SQLite

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nombre_completo_usuario VARCHAR,
    correo VARCHAR,
    fecha_registro TEXT
);

CREATE TABLE metodos_de_pago (
    id INTEGER PRIMARY KEY,
    tipo VARCHAR,
    nombre_banco varchar
);


CREATE TABLE productos (
    id INTEGER PRIMARY KEY NOT NULL,
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
    id INTEGER PRIMARY KEY,
    producto_id INT REFERENCES productos(id),
    usuario_id INT REFERENCES usuarios(id),
    comentario VARCHAR,
    calification INT,
    fecha_resena TEXT
);

CREATE TABLE facturas (
    id INTEGER PRIMARY KEY,
    metodos_de_pago_id INT REFERENCES metodos_de_pago(id),
    usuario_id INT REFERENCES usuarios(id),
    fecha_compra TEXT
);

CREATE TABLE factura_producto (
    id INTEGER PRIMARY KEY,
    numero_factura_id INT REFERENCES facturas(id),
    producto_id INT REFERENCES productos(id),
    cantidad_comprada INT,
    monto_total FLOAT
);


CREATE TABLE producto_carrito_compras (
    id INTEGER PRIMARY KEY,
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

# Modificar las tablas que contienen fechas para guardarlas en un tipo de dato especifico para fecha

De acuerdo a mi investigación una forma facil de usar un timestamp exacto es guardar la fecha en la base de datos utilizando epoch, el cual es un standard muy utilizado. 

UPDATE facturas SET fecha_compra = strftime('%s', '2026-03-10 10:30:56');
UPDATE productos SET fecha_ingreso = strftime('%s', '2026-03-10 10:30:56');
UPDATE resenas SET fecha_resena = strftime('%s', '2026-03-10 10:30:56');
UPDATE usuarios SET fecha_registro = strftime('%s', '2026-03-10 10:30:56');

1. **Crear categorías y ajustar productos**
- Cree la tabla `categories` con: `id` (PK autoincrement), `name` (UNIQUE, NOT NULL), `description`

CREATE TABLE categorias (
    id INT PRIMARY KEY,
    nombre_categoria TEXT UNIQUE NOT NULL,
    descripcion_categoria TEXT
);

- Agregue a `products` la columna `category_id` (INTEGER, puede permitir NULL)

ALTER TABLE productos ADD COLUMN categoria_id INT REFERENCES categorias(id);

- Inserte al menos 3 filas en `categories`

INSERT INTO categorias (id, nombre_categoria, descripcion_categoria) 
    VALUES (1, 'Gaming', 'Articulos pensados para jugar en PC o consolas de videojuegos')
    ;

INSERT INTO categorias (id, nombre_categoria, descripcion_categoria) 
    VALUES (2, 'Hogar', 'Articulos para el hogar')
    ;

INSERT INTO categorias (id, nombre_categoria, descripcion_categoria) 
    VALUES (3, 'Oficina', 'Articulos para la oficina')
    ;

- Actualice algunos `products` asignándoles un `category_id`

UPDATE productos SET categoria_id = 1 WHERE marca = 'Nintendo';
UPDATE productos SET categoria_id = 2 WHERE marca = 'Apple, Inc';
UPDATE productos SET categoria_id = 3 WHERE marca = 'Logitech';

- Verifique con `SELECT * FROM products (muestre: id, product_name, price, quantity, category_id);`

# Esta fue mi interpretación del ejercicio
SELECT 
productos.id, 
productos.nombre, 
productos.precio, 
productos.categoria_id,
SUM(factura_producto.cantidad_comprada) AS cantidad
FROM productos
JOIN factura_producto ON productos.id = factura_producto.producto_id 
GROUP BY 
productos.id, 
productos.nombre, 
productos.precio, 
productos.categoria_id;

# Se omite la columna cantidad ya que nunca fue requerida y se encuentra en tabla factura_producto, pero es otra cantidad y no la que posiblemente exigía el ejercicio. 
SELECT id, nombre, precio, categoria_id from productos;

2. **Carga de productos y filtros básicos**
- Inserte al menos **10** filas en `products` con `product_name`, `price`, `quantity` (no se usa cantidad)

INSERT INTO productos (nombre, precio)
    VALUES("Router", 500);

INSERT INTO productos (nombre, precio)
    VALUES("Switch", 200);

INSERT INTO productos (nombre, precio)
    VALUES("Silla", 1200);

INSERT INTO productos (nombre, precio)
    VALUES("Audifonos", 100);

INSERT INTO productos (nombre, precio)
    VALUES("Laptop", 5000);

INSERT INTO productos (nombre, precio)
    VALUES("Cable HDMI", 8);

INSERT INTO productos (nombre, precio)
    VALUES("Cable Ethernet", 16);

INSERT INTO productos (nombre, precio)
    VALUES("Servidor", 10000);

INSERT INTO productos (nombre, precio)
    VALUES("Luces Led Automaticas", 250);

INSERT INTO productos (nombre, precio)
    VALUES("Micro PC", 100);

# Me di cuenta que el ID no se estaba agregando de manera automatica, procedí a borrar las filas con el id `null`
# SQLite no hace el AUTOINCREMENT si el Primary Key no se crea con el type "INTEGER". INT != INTEGER para sqlite

DELETE from productos WHERE id is NULL;

- Seleccione todos los productos

SELECT * from productos; 

- Seleccione productos con `price > 50000`

SELECT * from productos WHERE price > 50000; -> ninguno estaba por encima de 50000 :( 
SELECT * from productos WHERE precio > 5000;

- Seleccione productos cuyo `product_name` contenga la palabra “apple” usando `LIKE`

SELECT * from productos where nombre LIKE 'apple'; -> ninguno estaba por encima de 50000 :( 
SELECT * from productos where nombre LIKE 'Micro%';

- Liste los **5** productos más caros con `ORDER BY price DESC LIMIT 5`

SELECT * from productos
ORDER BY precio DESC;

3. **Campos nuevos en facturas y actualización**
- Agregue a `invoices` las columnas `phone` (TEXT, puede ser NULL) y `cashier_code` (TEXT, por defecto `'N/A'`)

# Esto se había hecho en un paso anterior con los siguientes comandos. Sin embargo para cumplir con el ejercicio, tomé la dedisión de eliminar la tabla y volver a enviar los comandos actualizados.

ALTER TABLE facturas ADD COLUMN usuario_telefono int CHECK (usuario_telefono >= 10000000 AND usuario_telefono <= 99999999 );
ALTER TABLE facturas ADD COLUMN codigo_empleado TEXT DEFAULT 'N/A';

UPDATE facturas SET usuario_telefono int CHECK (usuario_telefono >= 10000000 AND usuario_telefono <= 99999999 ); -> Esto en teoría está correcto pero SQLite no lo reconoce

- Actualice varias facturas asignando valores a `phone` y `cashier_code`, esto ya se había hecho

INSERT INTO facturas (id, metodos_de_pago_id, usuario_id, fecha_compra, usuario_telefono, codigo_empleado) 
    VALUES (1, 1, 1, '10 de Marzo, 2026', 88881111, 'EMP01');

INSERT INTO facturas (id, metodos_de_pago_id, usuario_id, fecha_compra, usuario_telefono, codigo_empleado) 
    VALUES (2, 1, 1, '11 de Marzo, 2026', 88881111, 'EMP02');

INSERT INTO facturas (id, metodos_de_pago_id, usuario_id, fecha_compra, usuario_telefono, codigo_empleado) 
    VALUES (3, 1, 2, '12 de Marzo, 2026', 88882222, 'EMP01');

- Seleccione todas las facturas que tengan `phone` vacío o NULL

SELECT * FROM facturas WHERE usuario_telefono IS NULL;

- Seleccione una sola factura por `invoice_id`

SELECT * FROM facturas WHERE id = 1;

4. **Correcciones de datos en productos**

# Ya que quantity va a ser ignorado en la tabla productos, voy a utilizar `marca` como punto de referencia

- Establezca `quantity = 0` donde `price <= 0`

UPDATE productos SET precio = 200 WHERE marca = 'Logitech';

- Aumente el `price` en **100** unidades para todos los productos cuando `quantity` sea menor a 10

UPDATE productos SET precio = precio + 100 WHERE fecha_ingreso > 1773138600;

- Disminuya `quantity` en **1** para un `product_id` específico

UPDATE productos SET precio = precio - 1 WHERE id = 2;

- Verifique con `SELECT * FROM products ORDER BY id ASC LIMIT 10`

SELECT * FROM productos ORDER BY id ASC LIMIT 10;