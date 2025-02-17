"""Создание связи многие-ко-многим"""
CREATE TABLE PRODUCTS_ORDERS ( # инициируем таблицу
    product_order_id INT AUTO_INCREMENT NOT NULL, # атрибут увеличивается на 1 и предполагается к роли первичного ключа
    product TEXT(255) NOT NULL,
    in_order TEXT(255) NOT NULL,
    amount INT NOT NULL,

    PRIMARY KEY (product_order_id), # определяем атрибут в качестве первичного ключа
    FOREIGN KEY (product) REFERENCES PRODUCTS (product_id), # внешний ключ, ссылающийся на атрибут сторонней таблицы
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id() # внешний ключ, ссылающийся на атрибут сторонней таблицы
);



CREATE TABLE STAFF (
    staff_id INT AUTO_INCTEMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,
    PRIMARY KEY (staff_id),
);


CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCTEMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,
    PRIMARY KEY (product_id),
);

CREATE TABLE ORDERS (
    order_id INT AUTO_INCTEMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,
    PRIMARY KEY (order_id), # первичный ключ
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id) # определение внешнего ключа
);
