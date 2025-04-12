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