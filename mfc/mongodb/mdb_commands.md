### Команды для работы с MongoDB
- show dbs - отображение всех баз данных
- use mydb - создание базы данных
- show collections - просмотр всех коллекций

### CRUD
- db.createCollection('имя_коллекции', { опции }) - СОЗДАНИЕ коллекции

      db.createCollection('users', {
          capped: true, // Ограничение коллекции (capped - ограниченный)
          size: 5242880, // Максимальный размер в байтах
          maxDocuments: 5000 // Максимальное количество документов })
      })

- db.<имя_коллекции>.insertOne(документ) - ВСТАВКА ОДНОГО документа в коллекцию. Метод позволяет добавлять новый документ с уникальным `_id`, который создаётся автоматически в случае отсутствия.

      db.users.insertOne({
          name: 'John Doe',
          age: 30,
          email: "john.doe@example.com"
      })

- db.<имя_коллекции>.insertMany(документы, опции) - ВСТАВКА НЕСКОЛЬКИХ документов в коллекцию одновременно. Это позволяет эффективно добавлять множество записей за одну операцию, что может быть полезно для повышения производительности при массовой вствке данных.

      db.products.insetMany([
      { name: "Product A", price: 10.99, category: "Category 1" },
      { name: "Product B", price: 15.49, category: "Category 2" },
      { name: "Product C", price: 7.99, category: "Category 1" }
      ]) 
  
      // db.products.insertMany([{}, {}, {}]) сигнатура

- ОБНОВИТЬ ОДИН документ, добавив новое поле

      db.users.updateOne({_id: ...}, {$set: {newField: 'abc'}})
      db.users.findOne({_id: ObjectId('...')}) - посмотреть информацию о конкретном документе

- УДАЛЕНИЕ ПОЛЕЙ (оператор unset)

      db.users.updateOne({_id: ...}, {$unset: {newField: 'abc'}})
      
      
- ОБНОВИТЬ ОДИН созданный документ, ДОБАВИВ возможность создания поста ($push)

      db.users.updateOne({_id: ObjectId('67f26df01a2f15dc136b140e')}, {$push: {permissions: 'create_post'}})
      db.users.updateOne({_id: ObjectId('67f26df01a2f15dc136b140e')}, {$push: {permissions: 'delete_post'}})

- УДАЛИТЬ элементы из массива (pull)

      db.users.updateOne({_id: ObjectId('...')}, {$pull: {permissions: 'delete_post'}})

- ОБНОВИТЬ возраст У ВСЕХ пользователей, увеличив его на 1

      db.users.updateMany({}, {age: 1}) // {} - значит, все документы

- ПЕРЕИМЕНОВАТЬ поле 'address' для всех документов (где оно есть)

      db.users.updateMany({address: {$exists: true}}, {$rename: {'address': 'addrEEs'}})

- ПЕРЕИМЕНОВАТЬ ПОЛЕ 'Lisboa' на 'Moscow'

      db.users.updateMany(
            {'address.city': 'Lisboa'}, // Условия для поиска документа
            {$set: {'address.city': 'Moscow'}} // Обновление поля
        )

- db.<имя_коллекции>.drop() - УДАЛЕНИЕ коллекции и всех её документов

      db.myCollection.drop()

- db.<имя_коллекции>.deleteOne(<фильтр>) - УДАЛЕНИЕ ПЕРВОГО документа, соответствующего заданному фильтру. Если несколько документов, то будет удалён только один (первый найденный).

      db.users.deleteOne({ userId: 12345 })
 - db.<имя_коллекции>.deleteMany(<фильтр>) - УДАЛЯЕТ ВСЕ документы, соответствующие заданному фильтру

        db.users.deleteMany({ status: "inactive" })

- db.dropDatabase() - УДАЛЕНИЕ БАЗЫ ДАННЫХ

- db.<имя_коллекции>.find() - ПОЛУЧИТЬ ВСЕ ЗАПИСИ коллекции

            db.users.find()

- db.<имя_коллекции>.find().limit(2) - ОГРАНИЧЕНИЕ ВЫДАЧИ до 2 документов

            db.users.find().limit(2)

- db.<имя_коллекции>.find().limit(2).skip(1) - ВЫВОД документов, НАЧИНАЯ со второго

      db.users.find().limit(2).skip(1)

### Сортировка
- db.users.find().sort({ age: 1 }) - сортируем пользователей по НЕУБЫВАНИЮ (1 - сортировка по НЕУБЫВАНИЮ)
- db.users.find().sort({ age: -1 }) - сортируем пользователей по УБЫВАНИЮ (-1 - сортировка по УБЫВАНИЮ)

### Фильтрация записей
- Отображение информации о конкретном человеке

      db.users.find({name: 'Bob'})

- Найти пользователей возрастом не старше 31 (НЕ ВКЛЮЧИТЕЛЬНО)

      db.users.find({age: {$lt: 31}})

- Возвращаем только часть полей (name). "1" означает отображение данных в ответе

        db.users.find({age: {$lt:31}}, {name:1})

- Убираем `_id` из результатов выдачи

      db.users.find({age: {$lt:31}}, {name:1, _id:0})

- Найти пользователей НЕ СТАРШЕ 31 (ВКЛЮЧИТЕЛЬНО)

      db.users.find({age: {$lte:31}})

- Найти пользователей СТАРШЕ 31 (ВКЛЮЧИТЕЛЬНО)

      db.users.find({age: {$gte: 31}})

- Найти пользователей СТАРШЕ 31 (НЕ ВКЛЮЧИТЕЛЬНО)

      db.users.find({age: {$gt:31}})

### Поиск по наличию/отсутствию определённых полей в документе (н-р, найти документы с отсутствующим полем)
- Найти все документы С ПОЛЕМ email

      db.users.find({email: {$exists: true}})

- Найти все документы БЕЗ ПОЛЯ email

      db.users.find({email: {$exists:false}})

### Выборка с определёнными параметрами
- Найти пользователей с возрастом 19, 25 и 29 лет

      db.users.find({age: {$in: [19, 25, 29]}})

- Пользователи старше 18 (включительно) и младше 60 (включительно)

      db.users.find({age: {$gte:18, $lte: 60}})

### Логические операторы (and, not, or)
- Находим всех пользователей старше 20 И без email

      db.users.find({$and: [{age: {$gt: 20}}, {email: {$exists: false}}]})

      // эта запись эквивалентна вышестоящей
      db.users.find({age: {$gt:20}, email: {$exists:false}})

- Находим всех пользователей старше 20 ИЛИ без email
      
      db.users.find({$or: [{age: {$gt:20}}, {email: {$exists: false}}]})

- Находим все пользователей КРОМЕ 'Igor'

      db.users.find({name: {$not: {$eq: 'Igor'}}})

#### Добавление вложенной структуры данных

      db.users.insertOne({
            name: 'Tom',
            age: 33,
            address: {
            street: 'Avenida de Liberdade 1',
            city: 'Lisboa'
            }
            })

#### Поиск по вложенным полям
- Находим документы с городом Lisboa в поле адрес

      db.users.find({'address.city': 'Lisboa'})

- Находим КОЛИЧЕСТВО пользователей СТАРШЕ 30 лет

      db.users.countDocuments({age: {$gt: 30}})

      // Или (в старых версиях)
      db.users.count({age: {$gt:30}})

### Индексация (разобрать подробнее)
Индексы используются для ускорения запросов. <br>
Они особенно полезны, когда коллекции содержат большое количество документов и к этой коллекции приходится часто обращаться с однотипными запросами.

- Индекс на одно поле

      db.users.createIndex({age: 1})

- Индекс на группу полей

      db.users.createIndex({age: -1, name: 1})

- Просмотр всех индексов

      db.users.getIndexes()

- Удаление индексов

      db.users.dropIndex('age_-1_name_1')

Монго автоматически выбирает, какой индекс использовать для выполнения запроса. Можно использовать команду `explain` для анализа, как MongoDB использует индексы в запросах.

      db.users.find({age: {$exists: true}}).explain('executionStats')


### Агрегация 
-- Разобрать самостоятельно --
