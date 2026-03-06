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