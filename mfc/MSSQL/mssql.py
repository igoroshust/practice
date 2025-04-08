"""Что такое MS SQL?"""
# MS SQL - это полнофункциональная СУБД от Microsoft, предназначенная для хранения, управления и обработки структурированных и неструктурированных данных.

"""Команды"""
# CREATE DATABASE test_db;
# sp_databases; - список всех БД
# USE db_name; - выбрать БД для использования

# Подключение существующей БД
# CREATE DATABASE test_db
# ON PRIMARY(FILENAME='C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\test_db.mdf')
# FOR ATTACH;

# Удалить БД
# DROP DATABASE test_db;

# Удалить БД и завершением процесса
# ALTER DATABASE test_db SET OFFLINE;
# DROP DATABASE test_db

# Удалить таблицу
# DROP TABLE user_accounts

# Переименовать таблицу
# EXEC sp_rename 'старое_название_таблицы', 'новое_название';

# Вывести только уникальные фамилии с помощью DISTINCT
# SELECT DISTINCT surname from Users