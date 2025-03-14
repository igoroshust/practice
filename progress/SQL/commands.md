## Создание
CREATE - слово в SQL, использующееся для создания любых сущностей: таблиц, индексов, последовательностей и т.д.
CREATE TABLE users () - создать таблицу с пользователями. () - описание колонок таблицы

CREATE TABLE users (
    <название колонки> <тип данных> 
);

CREATE TABLE users (
    id BIGINT NOT NULL PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL
);

После жмём на кнопку отправки запроса в БД.

## Вставка
INSERT - слово в SQL, которое позволяет вставлять любые данные в любую таблицу в виде новой строчки в ней.
VALUES - слово в SQL, показывающее, какие именно значения будут вставляться для новой строчки в конкретные колонки.

INSERT INTO <НАЗВАНИЕ ТАБЛИЦЫ> (В какие колонки вставляем данные)
VALUES ()

INSERT INTO users (id, first_name, last_name, email)
VALUES (1, 'Igor', 'Oshust', 'igoroshust@yandex.ru');

INSERT INTO (id, first_name, last_name, email)
VALUES (2, 'Vera', 'Markova', 'vera@yandex.ru');

INSERT INTO (id, first_name, last_name, email)
VALUES (3, 'Stas', 'Soskov', 'stas@yandex.ru');