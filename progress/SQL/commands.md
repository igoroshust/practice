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


## JOIN
JOIN - слово, соединяющее две выборки из разных таблиц в единую выборку-результат.
Напирмер, когда в одной таблице мы хотим получить информацию из поля другой таблицы по FK.
JOIN - присоединение друг к другу колонок из разных таблиц. Мы как бы соединяем две таблицы в одну финальную выборку.
INNER JOIN - внутреннее объединение, OUTER JOIN - внешнее объединение.
LEFT OUTER JOIN - выбор всех строк, для которых не нашлось пары при объединении из левой таблицы. 
RIGHT OUTER JOIN - выборока строк без пары из правой таблицы.
FULL OUTER JOIN - используем, когда нужны строки без пар и из левой, и из правой таблицы.
Первая таблица в запросе - левая, вторая - правая.
ON - определение условия соединения строк из первой и второй таблицы между собой. 

SELECT * FROM <название таблицы>
JOIN <таблица, из которой получаем данные> ON <условие, определяющее, по какому принципу строка из 1 таблицы соединяется со строкой из 2>
... = <имя таблицы, к которой присоединяем>


SELECT * FROM spendings
JOIN users ON users.id (users - таблица, id - строчка) = spendings.user_id (spendings - имя таблицы, к которой присоединяем; user_id - колонка для соединения)

SELECT * FROM spendings
JOIN users ON users.id = spendings.user_id
~~ Результат: https://skrinshoter.ru/sUeMm5s2zJr

SELECT spendings.*, users.first_name FROM spendings
JOIN users ON users.id = spendings.user_id
~~ Результат: все колокни из spendings + first_name из users


## Агрегатные функции
Агрегатные функции - встроенные в SQL команды для подсчёта каких-либо общих значений из нескольких строк в таблицах.
SUM() - агрегатная функция, которая суммируем все значения в переданной колонке данной таблице в одно общее значение.

~~ Получаем суммарный прайс всех колонок в таблице
SELECT SUM(price) FROM spendings

~~ Получаем максимальный прайс во всей БД
SELECT MAX(price) FROM spendings

~~ GROUP BY
GROUP BY - Конструкция, определяющая колонки, по которым будет проводиться группировка результатов агрегатных функций.

SELECT SUM(price) FROM spendings
GROUP BY - после объявления функция должна применяться не ко всем строчкам в таблице, а считать отдельный результат для всех строк, в которых совпадает какое-либо значение.

SELECT SUM(price) FROM spendings
GROUP BY user_id
~~ Результат: группировка по user_id: https://skrinshoter.ru/sUeDbM91fGk

## HAVING
HAVING - слово, определяющее условия фильтрации с использованием агрегатных функций в выражениях.
HAVING специально создан для обработки условий по агрегатным функциям.
HAVING пишется только после GROUP BY.

~~ Показываем пользователей, у которых траты больше 5000

SELECT users.*, SUM(spendings.price) FROM users
JOIN spendings ON users.id = spendings.user_id
GROUP BY users.id, spendings.user_id
HAVING SUM(spendings.price) > 5000

## Изменение таблиц
ALTER TABLE - конструкция, позволяющая определять дополнительные команды для изменения любых ране созданных таблиц в БД

ALTER TABLE <таблица, которую хотим изменить> <как именно меняем таблицу> <имя колонки> <тип значений>

ALTER TABLE spendings ADD COLUMN category_id BIGINT;
~~ Формируем внешний ключ:
ALTER TABLE spendings ADD CONSTRAINT category_fk FOREIGN KEY (category_id) REFERENCES categories (id);
~ category_fk - Название правила
~ FOREIGN KEY - тип правила
~ category_id - из какой колонки в нашей таблице мы будем указывать на другую
~ REFERENCES categories (id) - на какую таблицу и колонку будем ссылаться.

ALTER TABLE spendings ADD COLUMN category_id BIGINT;
ALTER TABLE spendings ADD CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES categories (id);