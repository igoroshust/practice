1. Создаём сущность "Заказ"
CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATETIME NOT NULL,
    cost FLOAT NOT NULL,
    pickup INT NOT NULL,
    
    PRIMARY KEY (order_id) - создаём первичный ключ
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
);

# Базовые типы в SQL: INT, FLOAT, CHAR(size), TEXT, DATETIME
# AUTO_INCREMENT - указывает БД самостоятельно записать сюда значение.

2. Создаём сущность "Продукт"
CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    
    PRIMARY KEY (product_id)
);

3. Создаём сущность "Персонал"
CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,
    
    PRIMARY KEY (staff_id)
);

4. Создаём сущность "PRODUCTS_ORDERS"
CREATE TABLE PRODUCTS_ORDERS (
    products_order_id INT AUT0_INCREMENT NOT NULL,
    product INT NOT NULL,
    in_order INT NOT NULL,
    amount INT NOT NULL,

    PRIMARY KEY (products_order_id),
    FOREIGN KEY (product) REFERENCES PRODUCTS (products_id),
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id)
);



















