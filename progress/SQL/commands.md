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

### AS 
Используется для переименования столбца
rating AS difference - столбец будет difference
Новое имя является псевдонимом или алиасом - оно временное и не меняет реального имени столбца в БД
Если в алиасе есть пробелы, нужно заключать слово в двойные кавычки
rating AS "view difference"


### Неравенство <>
Проверяет, не равны ли два значения. Если значения не равны -> True, иначе -> False
Выбор всех пользователей КРОМЕ 30-летних

SELECT * FROM Users
WHERE age <> 30

### Комбинирование условий (AND и OR)
SELECT *
FROM sql.kinopoisk
WHERE year >= 2000
AND rating >= 8

SELECT
    year,
    movie_title,
    director
FROM sql.kinopoisk
WHERE (rating > 8.5 AND year < 2000) - скобки наделяют приоритетом
OR year >= 2000


### NOT (переворачивает следующий за ним оператор)
SELECT *
FROM sql.kinopoisk
WHERE year NOT BETWEEN 1965 AND 1980;


### IN
Оператор IN в SQL используется для проверки, содержится ли значение в заданном списке значений или подзапросе.
Это позволяет упростить запросы, когда нужно проверить несколько значений в одном условии.

Выбор пользователей с определённым идентификатором:
SELECT *
FROM Users
WHERE UserID IN (1, 2, 3);


### LIKE
Используется для поиска строк, которые соответствуют определённому шаблону.
Он часто применяется в условиях с `WHERE` для фильтрации данных на основе частичного совпадения
Используется, когда мы незначем наверняка, какое значение ищем

Синтаксис
SELECT column1, column2, ...
FROM table_name
WHERE column_name LIKE pattern;

В шаблонах, используемых с оператором LIKE, можно использовать следующие символы подстановки
- `%` - соответствует любому количеству символов (включая ноль)
- `_` - соответствует ровно одному символу

Задача: получить название всех фильмов, начинающихся на кириллическую 'A'
SELECT *
FROM sql.kinopoisk
WHERE movie_title LIKE 'A%'

- WHERE movie_title LIKE '%а%б%' выведет все фильмы, в названии которых встречается строчная 'a' и где-то после неё - 'б'.


### NULL
Специальное значение, указывающее на отсутствие данных или неизвестное значение. Равнозначно нолю или пустой строке.
Используется для обозначения отсутствия данных в столбце.
- `IS NULL` - проверяет, является ли значение `NULL`
- `IS NOT NULL` - проверяет, не является ли значение `NULL`

Задача: вернуть список пользователей с отсутствующим email
SELECT * FROM Users
WHERE email IS NULL;

Задача: вернуть список пользователей с email
SELECT * FROM Users
WHERE email IS NOT NULL;


### ORDER BY
ORDER BY необходим для задания порядка вывода строк в запросе.
ВАЖНО: ORDER BY идёт после применения всех условий в WHERE.
- `ASC` - явное указание сортировки ПО ВОЗРАСТАНИЮ (ascending - восходящий). Используется по умолчанию
- `DESC` - явное указание сортировки ПО УБЫВАНИЮ (descending - нисходящий)

В ORDER BY можно указывать расположение пустых значений (NULL) в начале или в конце с помощью:
- `NULLS FIRST`
- `NULLS LAST`

- Задача: отсортировать фильмы по названию в алфавитном порядке
SELECT *
FROM sql.kinopoisk
ORDER BY movie_title

SELECT *
FROM sql.kinopoisk
ORDER BY movie_title ASC

- Можно сортировать результат запроса по нескольким таблицам
SELECT 
    director,
    movie_title
FROM sql.kinopoisk
ORDER BY year, rating DESC

- Для упрощения работы с ORDER BY можно использовать не названия столбцов, а их номера из вывода.
- Сортировку по номеру столбца стоит использовать с осторожностью, поскольку при изменении вывода в SELECT всё может сбиться. 
- При добавлении новых столбцов в SELECT нужно проверить и при необходимости поправить номера столбцов в ORDER BY.

SELECT
    director,
    movie_title, 
    year
FROM sql.kinopoisk
ORDER BY 1, 3 DESC


### LIMIT
- LIMIT - ограничение вывода результатов запроса. Ключевое слово используется в самом конце запроса.
- Может использоваться для вывода топа для какого-либо показателя. 

Задача: ограничить вывод первыми 10 строками
SELECT *
FROM sql.kinopoisk
LIMIT 10


### OFFSET
- OFFSET - ОБРЕЗАЕТ указанное число первых строк, в то время как LIMIT - ОСТАВЛЯЕТ.
- LIMIT и OFFSET можно использовать вместе, их порядок неважен

Задача: вывести название и рейтинг фильмов с 4 по 8 место
SELECT
    movie_title,
    rating
FROM sql.kinopoisk
ORDER BY rating DESC
OFFSET 3 LIMIT 5 - (LIMIT отсчитывает количество строк после указанной в OFFSET строки)


### DISTINCT 
- DISTINCT (отчётливый, явный, отдельный) - ключевое слово в SQL, использующееся для удаления дубликатов из результатов запроса. 
- SQL возвращает только уникальные значения в выбранных столбцах.
DISTINCT пишется только 1 раз, в начале списка получаемых столбцов.

SELECT DISTINCT column_name
FROM table_name


### Агрегатные функции 
Агрегатные функции - это функции, выполняющие вычисления над множеством значений и возвращающих 1 значение.
Они часто используются в сочетании с оператором `GROUP BY` для группировки данных и получения сводной информации.

- COUNT() - подсчитывает количество строк в наборе данных
SELECT COUNT(*) FROM table_name;

- SUM() - вычисляет сумму значений в указанном столбце
SELECT SUM(column_name) FROM table_name;

- AVG() - вычисляет среднее значение для указанного столбца
SELECT AVG(column_name) FROM table_name;

- MIN() - возвращает минимальное значение в указанном столбце
SELECT MIN(column_name) FROM table_name;

- MAX() - возвращает максимальное значение в указанном столбце
SELECT MAX(column_name) FROM table_name;


### GROUP BY
GROUP BY - это оператор, который используется для группировки строк, имеющих одинаковые значения в указанных столбцах, и позволяет применять агрегатные функции к каждой группе
Это полезно, когда необходимо получить сводные данные, такие как суммы, средние значения, минимумы и максимумы для каждой группы.
GROUP BY нужен, чтобы посмотреть список с агрегированным.
GROUP BY пишется в самом конце и включает все колонки, которые не участвуют в агрегации.

SELECT
    pet,
    COUNT(quantity)
FROM for_aggregation
GROUP BY pet

- Запрос на отображение типов покемонов (два запроса аналогичны)
SELECT
    type1
FROM sql.pokemon
GROUP BY type1;

SELECT DISTINCT
    type1
FROM sql.pokemon;


### HAVING
HAVING используется для фильтрации уже агрегированных данных.
HAVING работает аналогично WHERE, только для агрегатных функций.
HAVING пишется в самом конце, даже после GROUP BY.

SELECT
    pet,
    count(*)
FROM for_aggregation
GROUP BY pet
HAVING COUNT(quantity) < 1