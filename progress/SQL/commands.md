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

## Обновление
UPDATE - ключевое слово, использующееся для обновления определённых значений определённых колонок в конкретных строках данной таблицы.
WHERE - слово, определяющее условие выборки конкретных строк для выполнения того или иного действия (чтения, обновления и т.д.)

UPDATE <название таблицы> SET 
<имя колонки> = <новое значение>, <имя колонки2> = <новое значение>
WHERE id = 1

UPDATE users SET
email = 'update@yandex.ru', first_name = 'Elon'

## Удаление
DELETE - слово, выполняющее удаление строк из данной таблицы, выбранных по какому-либо определённому условию.
DELETE FROM <имя таблицы>
WHERE <конкретные строчки>

DELETE FROM users
WHERE id = 2 OR id = 3 (удаляем 2 и 3)

## Удаление созданной таблицы
DROP TABLE <имя таблицы>;

## Извлечение данных
SELECT - слово, определяющее конкретные строки и колонки в данной таблице, которые необходимо выбрать (прочитать) из БД

SELECT <название колонки>, <название колонки> ... FROM <название таблицы>
WHERE <условие>

SELECT id, first_name, last_name, email FROM users
WHERE id = 1

## Оператор НЕ РАВНО <>
Оператор '<>' используется для сравнения значений и обозначается двумя способами: <> и !=
SELECT * FROM employees
WHERE department <> 'Sales'; - в этом примере будут выбраны все сотрудники, которые не работают в отделе "Sales".

## Связи между таблицами
FOREIGN KEY
CONSTRAINT - слово, определяющее новое правило организации данных в БД (связи, уникальность и т.д.)

CONSTRAINT <название правила> FOREIGN KEY (колонка(и) для внешнего ключа) REFERENCES <таблица> (ссылка на поле в другой таблице)


CREATE TABLE spendings (
	id BIGINT NOT NULL PRIMARY KEY,
	price INT NOT NULL,
	created_at TIMESTAMP DEFAULT now(),
	user_id BIGINT NOT NULL,

	CONSTRAINT users_id_fk FOREIGN KEY (user_id) REFERENCES users (id)
);
















## Добавить колонку в существующую таблицу
ALTER TABLE <название колонки>
ADD COLUMN user_id BIGINT NOT NULL;

## Добавить колонку + сформировать внешний ключ
ALTER TABLE users
ADD COLUMN user_id BIGINT,
ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

## Удалить колонку из существующей таблицы
ALTER TABLE <название колонки>
DROP COLUMN user_id;



## Вставить дату
INSERT INTO spendings (id, price, date)
VALUES(1, 4523, TO_DATE('12.10.2020', 'DD.MM.YYYY'));
