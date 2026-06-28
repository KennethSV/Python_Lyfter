INSERT INTO Users (name, email) VALUES
('Carlos Pérez', 'carlos.perez@email.com'),
('María Rojas', 'maria.rojas@email.com'),
('Jorge Vargas', 'jorge.vargas@email.com');

INSERT INTO Products (name, price, stock) VALUES
('Laptop Dell XPS 15', 1450.00, 10),
('Mouse Inalámbrico Logitech', 29.99, 50),
('Teclado Mecánico', 85.50, 30),
('Monitor LG 4K 27"', 320.00, 15),
('Cable HDMI 2.0 (2 metros)', 12.00, 100);

INSERT INTO Bills (user_id) VALUES

INSERT INTO Bill_Details (bill_id, product_id, quantity) VALUES
(1, 1, 1), 
(1, 5, 2); 

INSERT INTO Bill_Details (bill_id, product_id, quantity) VALUES
(2, 4, 1), 
(2, 3, 1), 
(2, 2, 1); 

INSERT INTO Bill_Details (bill_id, product_id, quantity) VALUES
(3, 4, 1);