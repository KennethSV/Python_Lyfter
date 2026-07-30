CREATE TABLE transactions.Users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);
 
CREATE TABLE transactions.Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock INT NOT NULL CHECK (stock >= 0)
);
 
CREATE TABLE transactions.Bills (
    bill_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Completada'
    CHECK (status IN ('Completada', 'Retornada')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES transactions.Users(user_id)
);
 
CREATE TABLE transactions.Bill_Details (
    detail_id  SERIAL PRIMARY KEY,
    bill_id    INT NOT NULL,
    product_id INT NOT NULL,
    quantity   INT NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (bill_id)    REFERENCES transactions.Bills(bill_id),
    FOREIGN KEY (product_id) REFERENCES transactions.Products(product_id),
    UNIQUE (bill_id, product_id)
);