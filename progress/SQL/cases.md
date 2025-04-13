### Напишите запрос, который выведет из таблицы kinopoisk следующие столбцы:
- имя режиссёра (director),
- название фильма (movie_title),
- разница между максимально возможным рейтингом (10) и рейтингом этого фильма.

SELECT 
    director,
    movie_title,
    10 - rating as difference
FROM sql.kinopoisk;


### Напишите запрос, который выведет из таблицы kinopoisk следующие столбцы 
- имя режиссёра, 
- название фильма, 
- рейтингом по 100-балльной шкале (столбец rating_100). 
Рейтинг по 100-балльной шкале определите как оценку по 10-балльной, умноженную на 10.

SELECT
    director,
    movie_title,
    rating * 10 AS rating_100
FROM sql.kinopoisk;


### Вывести все столбцы для всех фильмов, КРОМЕ снятых в 2000 году
SELECT *
FROM sql.kinopoisk
WHERE year <> 2000


### Выбрать фильм, используя комбинирование условий
SELECT *
FROM sql.kinopoisk
WHERE year >= 2000
AND rating >= 8


### Выбрать фильм между 1975 и 1985 годами
SELECT *
FROM sql.kinopoisk
WHERE year BETWEEN 1975 AND 1985;

Либо:
SELECT *
FROM sql.kinopoisk
WHERE year >= 1975
AND year <= 1985;


### Выведите количество фильмов с рейтингом от 8.5 до 8.7
SELECT
    COUNT(movie_title)
FROM sql.kinopoisk
WHERE rating BETWEEN 8.5 AND 8.7;


### Вывести все фильмы кроме вышедших с 1965 по 1980 годы
SELECT *
FROM sql.kinopoisk
WHERE year NOT BETWEEN 1965 AND 1980;


### Выбор пользователей с определённым идентификатором
SELECT *
FROM Users
WHERE UserID IN (1, 2, 3);


### Вывести название фильмов, вышедших в 1939, 1985 и 2000 годах
SELECT
    movie_title
FROM sql.kinopoisk
WHERE year IN (1939, 1985, 2000);

### Получить название всех фильмов, начинающихся на кириллическую 'A'
SELECT *
FROM sql.kinopoisk
WHERE movie_title LIKE 'A%';


### Напишите запрос, чтобы вывести название и год выпуска в прокат тех фильмов, которые были сняты режиссёром по имени Дэвид (то есть значение в поле director начинается с 'Дэвид') и имеют рейтинг больше 8.
SELECT movie_title, year
FROM sql.kinopoisk
WHERE director LIKE 'Дэвид%'
AND rating >= 8;

### Отсортировать фильмы по названию в алфавитном порядке (по возрастанию)
SELECT *
FROM sql.kinopoisk
ORDER BY movie_title

Вышестоящая запись аналогична этой:
SELECT *
FROM Users
ORDER BY movie_title ASC


### Вывести названия, имена режисёров и сценаристов, и дату фильмов, выпущенных в СССР + отсортировать по убыванию
SELECT
    movie_title,
    director,
    screenwriter,
    year
FROM sql.kinopoisk
WHERE country = 'СССР'
ORDER BY rating DESC


### Напишите запрос, который выведет столбцы с названием фильма, его описанием и годом выхода в прокат. 
- Оставьте только те фильмы, у которых рейтинг не ниже 8.2 и страна производства — не США. 
- Отсортируйте вывод по году выхода фильма в порядке убывания.

SELECT
    movie_title,
    overview,
    year
FROM sql.kinopoisk
WHERE rating >= 8.2 AND country <> 'США'
ORDER BY year DESC;


### Напишите запрос, чтобы вывести названия всех фильмов (столбец Название фильма), у которых рейтинг выше 8.3 и страна производства — Франция. 
- Отсортируйте по рейтингу в порядке убывания, далее — по году выхода в прокат (также в порядке убывания).

SELECT movie_title
FROM sql.kinopoisk
WHERE rating >= 8.3 AND country = 'Франция'
ORDER BY rating DESC, year DESC;


### Ограничить вывод первыми 10 строками
SELECT *
FROM sql.kinopoisk
LIMIT 10


### Вывести ТОП-5 фильмов по рейтингу, сперва отсортировав их по убыванию, оставив только верхние 5 строк
SELECT 
    movie_title,
    rating
FROM sql.kinopoisk
ORDER BY rating DESC
LIMIT 5;


### Напишите запрос, который выводит информацию (Режиссёр, Название фильма и Актёры) 
- по ТОП-20 самых старых (определяем по году выхода в прокат) фильмов из таблицы kinopoisk.

SELECT
    director,
    movie_title,
    actors
FROM sql.kinopoisk
ORDER BY year ASC
LIMIT 20;


### Вывести название и рейтинг фильмов с 4 по 8 место
SELECT
    movie_title,
    rating
FROM sql.kinopoisk
ORDER BY rating DESC
OFFSET 3 LIMIT 5 - (LIMIT отсчитывает количество строк после указанной в OFFSET строки)


### Напишите запрос, чтобы вывести названия фильмов, которые вышли в прокат после 1990 года и были сняты не в России. 
- Из этого списка оставьте только те фильмы, которые занимают с 20 по 47 места в рейтинге. 
- Отсортируйте результат по убыванию рейтинга фильмов.

SELECT 
    movie_title
FROM sql.kinopoisk
WHERE (county <> 'Россия' AND year > 1990)
ORDER BY rating DESC
OFFSET 19 LIMIT 28;


### Какой режиссёр снял самый старый фильм в списке?
SELECT director
FROM sql.kinopoisk
ORDER BY year
LIMIT 1;


### В каком году был выпущен фильм, который занимает 111 строку в списке, отсортированном по рейтингу в порядке убывания?
SELECT year 
FROM sql.kinopoisk
ORDER BY rating DESC
OFFSET 110 LIMIT 1


### Напишите запрос, который выводит столбцы «Название фильма» (movie_title), «Режиссёр» (director), «Сценарист» (screenwriter), «Актёры» (actors). 
Оставьте только те фильмы, у которых:
- рейтинг между 8 и 8.5 (включительно) ИЛИ год выхода в прокат до 1990;
- есть описание;
- название начинается не с буквы 'Т';
- название состоит ровно из 12 символов.
- Оставьте только топ-7 фильмов, отсортированных по убыванию рейтинга.

SELECT 
    movie_title,
    director,
    screenwriter,
    actors
FROM sql.kinopoisk
WHERE (
        (rating BETWEEN 8 AND 8.5) OR (year < 1990)
      ) AND
    overview IS NOT NULL AND
    movie_title NOT LIKE 'Т%' AND
    LENGTH(movie_title) = 12
ORDER BY rating DESC
LIMIT 7;


### Подсчитать количество строк в таблице (используем агрегатные функции)
SELECT
    COUNT(*) -- звёздочка означет подсчёт всех строк, которые возвращает запрос
FROM sql.pokemon


### Подсчитать количество уникальных значений
SELECT
    COUNT(DISTINCT type1)
FROM sql.pokemon;


### Определить среднее количество очков здоровья у покемонов-драконов
SELECT
    AVG(hp)
FROM sql.pokemon
WHERE type1 = 'Dragon';


### Несколько агрегатных функций в одном запросе
SELECT
    COUNT(*) AS 'Всего травяных покемонов',
    COUNT(type2) AS 'Покемонов с дополнительным типом',
    AVG(attack) AS 'Средняя атака',
    AVG(defense) AS 'Средняя защита'
FROM sql.pokemon
WHERE type1 = 'Grass'


### Напишите запрос, который выведет:
- количество покемонов (столбец pokemon_count),
- среднюю скорость (столбец avg_speed),
- максимальное и минимальное число очков здоровья (столбцы max_hp и min_hp)
- для электрических (Electric) покемонов, имеющих дополнительный тип и показатели атаки или защиты больше 50.

SELECT
    COUNT(pokemon) AS "pokemon_count",
    AVG(speed) AS "avg_speed",
    MAX(hp) AS "max_hp",
    MIN(hp) AS "min_hp"
FROM sql.pokemon
WHERE type1 = 'Electric'
    AND type2 IS NOT NULL
    AND (attack > 50 OR defense > 50);


### Подсчитать количество типов покемонов
SELECT
    type1,
    type2,
    COUNT(*)
FROM sql.pokemon
GROUP BY type1, type2
ORDER BY type1, type2 NULLS FIRST -- сортировка по алфавиту (необзяательно)
-- ORDER BY COUNT(*) DESC -- сортировка в обратном порядке по количеству


### Напишите запрос, который выведет:
- число различных дополнительных типов (столбец additional_types_count),
- среднее число очков здоровья (столбец avg_hp),
- сумму показателей атаки (столбец attack_sum) в разбивке по основным типам (столбец primary_type).
- Отсортируйте результат по числу дополнительных типов в порядке убывания, при равенстве — по основному типу в алфавитном порядке. 
- Столбцы к выводу (обратите внимание на порядок!): primary_type, additional_types_count, avg_hp, attack_sum.

SELECT
    type1 AS primary_type,
    COUNT(DISTINCT type2) AS additional_types_count,
    AVG(hp) AS avg_hp,
    SUM(attack) AS attack_sum
FROM sql.pokemon
WHERE type2 IS NOT NULL
GROUP BY type1
ORDER BY additional_types_count DESC, primary_type ASC;