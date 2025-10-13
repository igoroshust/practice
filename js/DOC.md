####
JS - ЯП с динамической типизацией (не нужно объявлять тип хранимого значения заранее).
```
let someVariable = 'Some value';
someVaruable = 50;
someVariable = true;
```

#### Переменные
- var - устаревший способ, имеет функциональную область видимости (внутри функции или глобально)
+ переменные доступны до их объявления. Может быть переопределена в той же области видимости.
```javascript
// допустимо (повторное объявление)
var x = 1;
var x = 2;
```

- let - современный способ, имеет блочную область видимости (внутри фигурных скобок {}) + нельзя обратить до объявления
+ нельзя повторно обратиться в той же области видимости
```javascript
// недопустимо (повторное объявление)
let x = 1;
let x = 2;

// допустимо (переопределение)
let y = 1;
y = 2;
```

Разница наглядно
```
{
  let userName = "Bob";
  console.log(userName);
  
  var someNumber = 10;
  console.log(someNumber);
}

console.log(userName); // Ошибка ReferenceError
console.log(someNumber); // 10
```


- const - используется для объявления констант, значение которых не может быть изменено.

```
let name = 'Alice'
const age = 30;
```


#### Типы данных
- Строка (String)
- Число (Number)
- Логический (Boolean)
- Ничего (Null) - значение переменной, присаиваемое разработчиком, как намеренно пустое. 
```
let age = 32;
age = null; // сброс значения
```
- Не определённое значение (undefined). Когда объявили переменную, но не передали в неё значение.
Когда функция срабатывает, но мы не прописали, что она будет возвращать, она вернёт undefined.
А также undefined вернётся в случае неудовлетворительного поиска (например, элементов на странице)
Или при обращении к несуществующему объекту аналогично срабатывает undefined
```
let test;
console.log(typeof(test)); // undefined
```
Для обнуления используем `undefined` вместо `null`
```
let someName = 'James';
someName = undefined; // НЕПРАВИЛЬНО
someName = null; // Правильно
```

**Отличие null от undefined**
null явно задаётся разработчиком, undefined автоматически присваивается JavaScript.

- BigInt - встроенный объект, позволяющий создавать большие числа. Дописываем "n" в конце числа.
Не может быть смешан с другими типами, нужно использовать только в операциях с BigInt.
```
console.log(12930123012301923012n); // BigInt
12930123012301923012n + 12931239192n // корректно;
```

```
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991 (16-ти значное число)
``` 

- symbol - создание уникальных идентификаторов для имён свойств в объектах. 
Это уникальное примитивное значение, позволяющее добавлять уникальное свойство к объекту, с уверенностью, что он не
перезапишет никакое другое свойство.
Не участвует в циле for in.
```
const sym = Symbol();
const symWithDesc = Symbol('описание');
```

Использование symbol
```
const id = Symbol('id');
const user = {
    name: 'Иван'
    [id]: 123
};
```

- Массив (Array) - упорядоченная коллекция элементом, доступ к которым осуществляется по индексу.
Используется для упорядоченных данных.

```
// Литеральный способ
const arr1 = [1, 2, 3];

// Конструктор Array
const arr2 = new Array(1, 2, 3)
```
**Основные характеристики**
1) Могут изменять размер
2) Индексация начинается с 0
3) Могут содержать элементы разных типов
4) Элементы можно добавлять, удалять и изменять

**Методы работы с массивами**
1) Добавление и удаление
```
arr.push(4); // Добавление элемента в конец
arr.pop(); // Удаление последнего элемента
arr.shift(); // Удаление первого элемента
arr.unshift(0); // Добавление в начало
```

2) Поиск и фильтрация
```
arr.indexOf(2); // Поиск индекса
arr.includes(2); // Проверка наличия
arr.filter(x => x > 1); // Фильтрация
```

3) Преобразование
```
arr.map(x => x * 2) // Преобразование
arr.reduce((a, b) => a + b); // Суммирование
```

4) Другие
```
.splice()
.slice()
.forEach()
.reverse()
```

**Метод splice()**
Метод массива, позволяющий изменять содержимое массива, добавляя, заменяя или удаляя элементы
`array.splice(start[, deleteCount[, item1[, item2[, ...]]]])`
start - индекс начала изменений
deleteCount - количество удаляемых элементов (необязательный)
item1, item2 - элементы для добавления (необязательные параметры)

Удаление элементов
```
const arr = [1, 2, 3, 4, 5];
arr.splice(2, 2); // Удаляет 2 элемента, начиная с индекса 2
console.log(arr); // [1, 2, 5]
```

Добавление элементов
```
const arr = [1, 2, 5];
arr.splice(2, 0, 3, 4); // Добавляет элементы 3 и 4 на позицию 2
console.log(arr); [1, 2, 3, 4, 5]
```

Замена элементов
```
const arr = [1, 2, 3, 4, 5];
arr.splice(2, 2, 'a', 'b'); // Заменяет 2 элемента на 'a' и 'b'
console.log(arr); // [1, 2, 'a', 'b', 5]
```

**Метод .forEach()**
```
const autoBrands = ['a', 'b', 'c'];
autoBrands.forEach(функция, применяемая к каждому элементу(){
    // Тело функции;
});
```

Функция внутри forEach
```
const autoBrands = ['a', 'b', 'c']

autoBrands.forEach(function(item, index){ // (item, index) - индекс вторым параметром
  console.log(`${index} => ${item}`);
});
```

Сторонняя функция в forEach
```
const autoBrands = ['a', 'b', 'c']

function getBrand(item, index){
    console.log(`${index} -> ${item}`);
}

autoBrands.forEach(getBrand);
```

forEach со стрелочной функцией
```
const autoBrands = ['a', 'b', 'c'];
autoBrands.forEach((brand, i) => console.log(`${brand} => ${i}`));
```

**Метод filter()**
Создание нового массива с элементами, удовлетворяющими условию:
```
const arr = [1, 2, 3, 4, 5];
const filtered = arr.filter(x => x > 2);
console.log(filtered); // [3, 4, 5]
```

**Метод map()**
Создание нового массива с преобразованными элементами
```
const arr = [1, 2, 3, 4, 5];
const doubled = arr.map(x => x * 2);
console.log(doubled); // [2, 4, 6, 8]
```

**Метод reduce()**
Сворачивание массива в одно значение

Найти сумму элементов
```
const arr = [1, 2, 3, 4, 5];
let result = arr.reduce((a, b) => a + b);
console.log(result); // 15
```






- Объекты (Object) - неупорядоченная коллекция свойств (пар ключ-значение). Используется для связанных данных.
```
// Литеральный способ
const obj1 = {
    name: 'Иван',
    age: 25,
    isStudent: true
};

// Конструктор Object
const obj2 = new Object();
obj2.name = 'Иван';
```

Особенности:
1) Состоят из ключей (строк) и значений (любых типов)
2) Можно добавлять/удалять свойства
3) Могут содержать другие объекты и массивы
4) Могут содержать функции

Доступ к свойствам
```
obj.name // Через точку
obj['name'] // Через квадртаные скобки
```

Перебор свойств
```
for (let key in obj) {
    console.log(key, obj[key]);
}
```

Проверка свойства
`obj.hasOwnProperty('name')`

#### Сравнение значений
```
console.log('5' == 5); // true
console.log('5' === 5); // false
```

#### if else
```
let time = 15;

if (time > 12) {
  console.log('Добрый день');
} else if (time >= 12 && time < 18) {
  console.log('Доброе утро');
} else {
  console.log('Добрый вечер');
}
```

#### Логические операторы
`&&` - Логическое И
`||` - Логическое ИЛИ
`!` - Логическое НЕ


#### Тернарный оператор
`(условие) ? (условие верно) : (условие неверно);`

```
10 < 12 ? console.log('Условие верно') : сonsole.log('Условие неверно');
```

Присвоение значения переменной с использованием тернарного оператора
```
greeting = time < 12 ? 'Доброе утро' : 'Добрый день';
```

#### Конкатенация строк и шаблонные строки
```
let userName = 'Игорь';
let greeting = 'Привет, Марк!';
let howAreYou = 'Как твои дела?';


let sayHi = greeting + ' ' + howAreYou;
let sayHello = 'Привет, ' + userName + howAreYou;
let sayHitemplate = `${greeting} ${howAreYou}`;
console.log(sayHi);
```

#### Функции
```
// function declaration
function sayHello(name) {
  return 'Привет, ' + name + '!';
}

console.log(sayHello('Igor'));


// function expression
const sayHi = function() {
  return name + '!';
}

console.log(sayHi('igor'))
```

**function declaration**
Это классический способ объявления функции
```
function test(testValue) {
    return testValue;
}
```
1) Можем вызывать функцию до момента её объявления (связано со считыванием JS файла несколько раз);
Например, такой способ применим при создании публичных API.
2) Можем сперва описать работу программы (вызовы), а ниже привести примеры кода;
``` 
sayHi();

function sayHi(name) {
    return name;
}
```
3) Не может быть присвоена переменной напрямую
4) Короче и лаконичнее

**function expression**
Функция создаётся как значение выражения
```
const test = function(testValue) {
    return testValue;
}
```
1) Нельзя вызвать перед объявлением
2) Может быть анонимной;
3) Можно присвоить переменной
4) Предъявляет более строгие правила к объявлению функций;

Используем при:
1) Присваивании функциям переменных
2) В коллбеках
3) Когда функция нужна только в определённой области видимости

**Стрелочные функции (Arrow Functions)**
Современный компактный синтаксис для создания функций.
`const greet = name => console.log('Привет, ' + name);`

1) Более короткий формат записи
2) Неявное возвращение для однострочных функций
3) Автоматическое связывание this
4) Нет собственного this

`const add = (a, b) => a + b;`

Используем стрелочные функции:
1) В коллбеках и обработчиках;
2) Когда важен контекст this
3) Для коротких функций
4) При работе с массивами (map, filter)


**Анонимная функция**
Анонимная функция - функция без имени, которая обычно создаётся как часть выражения.
```
let adder = function(a, b) {
    return a * b;
};

// Использование в методах массивов
[1, 2, 3].forEach(function(число) {
    console.log(число);
})
```


#### Коллбэк (Callback)
Функция, которая передаётся другой функции в качестве аргумента и выполняется после завершения определённой операции.

Таймер
```
function greet() {
    console.log('Привет');
}

// Передаём функцию greet как колбек
setTimeout(greet, 2000);
```

Обработка данных
```
function fetchData(callback) {
    setTimeout(() => {
        const data = {
            id: 1,
            name: 'Иван'
        };
        callback(null, data); // null означает отсутствие ошибки
    }, 1000);
}

// Использование колбэка
fetchData((error, data) => {
    if (error) {
        console.error('Ошибка: ', error);
    } else {
        console.log('Полученные данные: ', data);
    }
});

```

Пример
```
function summ(a, b) {
  return a + b;
}

function diff (a, b) {
  return a - b;
}

function doSomething(func) {
  let x = 10;
  let y = 15;
  let result = func(x, y);
  return result;
}

console.log(doSomething(summ));
console.log(doSomething(diff));
```

Коллбек - функция, которую мы передали в качестве аргумента и которая вызывается внутри другой функции.

**Самовызывающаяся функция IIFE**
Immediately invoked function expression - незамедлительное выполнение функции (вызов самой себя)
```
(function (){
    console.log('Привет, дорогой пользователь!');
})(); // точка с запятой обязательна

// (функция)() -- скобки для вызова
```

Вызов самовызывающейся функции с передачей в неё аргументов
```
let res = (function summ(a, b){
    console.log(a);
    console.log(b);
    console.log(a + b);
})(10, 15);
```

Применение:
1) Ограничение области видимости (старый стандарт ES5);
2) Запуск скрипта сразу при запуске страницы;
3) Для выполнения однократных операций;
4) При настройке соединения с сервером;
5) Сохранение приватных переменных
6) Защита от конфликтов имён
7) Организация безопасного пространства для работы с данными


**Стрелочная функция**

```
const arrSayHi = (name) => {
    console.log(`Привет, ${name}! Как твои дела?`);
}
```

Стрелочная функция НЕ ИМЕЕТ своего контекста и ссылается на контекст той области, в которой она была объявлена.




#### Промисы
Промис - это объект, представляющий результат асинхронной операции.
Состояние:
1) Pending (ожидание)
2) Fulfilled (выполнено успешно)
3) Rejected (отклонено)

Пример промиса
```
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = {
                message: 'Данные получены'
            };
            resolve(data); // Успешное выполнение
            // reject(new Error('Ошибка при получении данных'));
        }, 1000);
    });
}

fetchData()
    .then(data => {
        console.log('Успех: ', data)
    })
    .catch(error => {
        console.error('Ошибка: ', error);
    });
```

#### Контекст this
this определяет, на какой объект ссылается ключевое слово this в момент выполнения функции



#### Массивы
Коллекция данных (Структура данных). Можно записывать данные разных типов, но не рекомендуется.

`const autoBrands = ['a', 'b', 'c', 'd']`

Вывод количества элементов в массиве:
`console.log(autoBrands.length); // 4`


#### Цикл for
```
for (начальное значение счётчика; условие; итератор (то, как будет изменяться счётчик после итерации){
    // Тело цикла
}
```

```
for (let i = 1; i <= 10; i++){
  console.log(i);
}
```


#### Цикл for of 
Обход массива с помощью цикла for of (все элементы массива)
```
const autoBrands = ['a', 'b', 'c']

for (let item of autoBrands) {
  console.log(item);
}
```

В цикле for явный перебор счётчика, for of обходит элементы последовательно.


#### Объекты
Объект - набор свойств (пар ключ-значение), где ключи являются строками (или символами), а значения могут быть любого
типа данных. Это структура данных, позволяющая организовать данные определённым образом.

```
const person = {
  userName: 'Марк',
  age: 30,
  isMarried: false,
  test: {
    a: 1
  }
};

// Создаём новое свойство
person.profession = 'Designer';

// Удаляем свойство
delete person.profession;

console.log(person);
console.log(person.test.a); // 1
console.log(person['test']['a']); // 1
```

#### Методы в объектах
Свойство объекта, которое записано в функцию, называется методом объекта.

```
const person = {
  userName: 'Марк',
  age: 30,
  isMarried: false,
  
  // Метод объекта
  sayHi: function(name) {
    console.log('Привет, ' + name);
  }
};

// Вызов метода
person.sayHi('Игорь');

// Создание метода
person.sayBye = function(name){
  console.log('Пока, ' + name);
}

person.sayBye('Игорь');
```

**this**
Ключевое слово `this` внутри метода объекта ссылается на сам объект
```
const person = {
  userName: 'Марк',
  age: 30,
  isMarried: false,
  sayHi: function(name) {
    console.log(`Привет, ${name}. Меня зовут ${this.userName}`);
  }
};

// Вызов метода
person.sayHi('Игорь');
```

#### Обход объектов через for in (не путать с for of для обхода массивов)
for in нужен для обхода объектов. В отличии от for of, может обходить неитерируемые объекты. Возвращает ключи.

```
const person = {
  userName: 'Марк',
  age: 30,
  isMarried: false,
  sayHi: function(name) {
    console.log(this);
    console.log(`Привет, ${name}. Меня зовут ${this.userName}.`);
  }
};

for (let key in person) {
  console.log(key);
  console.log(key, ':', person[key]);
}

// Вывод:
"userName"
"age"
"isMarried"
"sayHi"
```

#### Методы объектов
- Object.keys() — возвращает массив собственных перечисляемых свойств объекта:
```
const obj = { a: 1, b: 2 };
console.log(Object.keys(obj)); // ['a', 'b']
```

- Object.values() — возвращает массив значений собственных перечисляемых свойств:
```
const obj = { a: 1, b: 2 };
console.log(Object.values(obj)); // [1, 2]
```

- Object.entries() — возвращает массив пар [ключ, значение]:
```
const obj = { a: 1, b: 2 };
console.log(Object.entries(obj)); // [['a', 1], ['b', 2]]
```

- Object.assign() — копирует значения всех собственных перечисляемых свойств из одного или более исходных объектов в целевой объект:
```
const target = { a: 1 };
const source = { b: 2 };
const result = Object.assign(target, source);
// result = { a: 1, b: 2 }
```

- Object.create() — создаёт новый объект с указанным прототипом:
```
const proto = { greeting: 'Hello' };
const obj = Object.create(proto);
console.log(obj.greeting); // Hello
```

- Object.getPrototypeOf() — возвращает прототип указанного объекта:
```
const obj = {};
console.log(Object.getPrototypeOf(obj)); // Object {}
```

- Object.setPrototypeOf() — устанавливает прототип объекта:
```
const proto = {};
const obj = {};
Object.setPrototypeOf(obj, proto);
```

Методы для проверки и работы со свойствами
- Object.defineProperty() — определяет новое свойство непосредственно в объекте или изменяет существующие:
```
const obj = {};
Object.defineProperty(obj, 'name', {
 value: 'Иван',
 writable: false
});
```

- Object.defineProperties() — определяет несколько свойств для объекта:
```
const obj = {};
Object.defineProperties(obj, {
 name: { value: 'Иван' },
 age: { value: 25 }
});
```

- Object.getOwnPropertyDescriptor() — возвращает объект, описывающий свойство:
```
const obj = { name: 'Иван' };
console.log(Object.getOwnPropertyDescriptor(obj, 'name'));
```

- Object.seal() — предотвращает создание новых свойств объекта и делает все существующие свойства не конфигурируемыми:
```
const obj = { a: 1 };
Object.seal(obj);
```

- Object.freeze() — замораживает объект, делая его неизменяемым:
```
const obj = { a: 1 };
Object.freeze(obj);
```

- Object.isSealed() — проверяет, запечатан ли объект:
```
const obj = {};
console.log(Object.isSealed(obj)); // false
```

- Object.isFrozen() — проверяет, заморожен ли объект:
```
const obj = {};
console.log(Object.isFrozen(obj)); // false
```

- Object.isExtensible() — проверяет, можно ли добавлять новые свойства в объект:
```
const obj = {};
console.log(Object.isExtensible(obj)); // true
```

Методы для проверки
- Object.prototype.hasOwnProperty() — проверяет, содержит ли объект указанное свойство как собственное:
```
const obj = { a: 1 };
console.log(obj.hasOwnProperty('a')); // true
```

- Object.prototype.propertyIsEnumerable() — проверяет, является ли свойство перечисляемым:
```
const obj = { a: 1 };
console.log(obj.propertyIsEnumerable('a')); // true
```

- Object.prototype.toString() — возвращает строковое представление объекта:
```
const obj = {};
console.log(obj.toString()); // [object Object]
```

- Object.prototype.valueOf() — возвращает примитивное значение объекта:



#### Классы (конструкторы объектов)
Класс - это как чертёж для всех будущих объектов (например, person), которые будут созданы на его основе.
Конструктор - функция, создающая объекты, и наполняющая их данными (свойствами).

```
class Person {
  constructor(userName, age, isMarried){
    this.userName = userName;
    this.age = age;
    this.isMarried = isMarried;
  }
  
  sayHi(name) {
    console.log('Привет, ' + name + '. Я - ' + this.userName);
  }
};

// Создаём экземпляр класса Person
const person1 = new Person('Марк', 30, false);
const person2 = new Person('Павел', 28, true);
console.log(person1);
console.log(person2);

person2.sayHi('Igor');
```









#### Подробнее про
setTimeout
setInterval
date
this
Встроенные функции
Асинхронность в JS
Библиотеки JS
fetch().then().catch()
try catch
Стек и очередь на примере JS
Приведение типов в JS























