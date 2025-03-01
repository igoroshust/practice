1. Создаём сущность "Заказ"
CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATETIME NOT NULL,
    cost FLOAT NOT NULL,
    pickup INT NOT NULL
);

# Базовые типы в SQL: INT, FLOAT, CHAR(size), TEXT, DATETIME
# AUTO_INCREMENT - указывает БД самостоятельно записать сюда значение.

2. Создаём сущность "Продукт"
CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL
);

3. Создаём сущность "Персонал"
CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL
);