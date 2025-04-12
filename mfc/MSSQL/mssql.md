### Просмотр всех таблиц в базе данных
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';

### Удалить запись из существующей таблицы
DELETE FROM <имя_таблицы> WHERE условие;

DELETE FROM Users WHERE UserID = 1;