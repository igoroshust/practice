/* Выбор DOM-элементов */
/* Прослушка событий */

const button = document.querySelector('#button');
const button1 = document.querySelector('#button1');
const picture1 = document.querySelector('#picture');

button.value = 'Удалить';

// Устанавливаем прослушку события (удаление по клику)
// addEventListener позволяет навешивать много обработчиков на 1 событие
button.addEventListener('click', function(){
    console.log('Click!');
    picture1.remove(); // Удаляем картинку
});

// { capture: true } - действия на этапе захвата (будет выведено перед кликом)
button.addEventListener('click', function(){
    console.log('Захват!');
}, { capture: true });

// { once: true } - обработчик выполняется только один раз, затем автоматически удаляется. 
// Полезно для одноразовых действий с целью избежать утечек в памяти.
button1.addEventListener('click', function(){
    console.log('1 раз выполнюсь');
}, { once: true });

// { passive: true } - обработчик не будет вызывать `preventDefault()` (запрет стандартного поведения, например, прокрутки)
window.addEventListener('scroll', () => console.log('Скролл'), { passive: true })

button1.addEventListener('click', (e) => {
    e.preventDefault(); // Работает только при passive: false
    console.log('Клик без действия по умолчанию');
}, { passive: false });


// { signal: undefined } - позволяет отменить слушатель с помощью AbortController. Полезно для очистки при размонитровании компонентов (например, в React)
// signal отменяет только те обработчики, которые явно связаны с ним.
const controller = new AbortController();
button.addEventListener('click', () => console.log('Клик из signal'), { signal: controller.signal })

// Отмена всех связанных слушателей (через 2 секунды сигнал отменится)
setTimeout(() => {
    controller.abort();
    console.log('Сигнал отменён!');
}, 2000)


// Альтернативный способ навешивать события по клику
// Только 1 обработчик (дубли перезаписывают исходный). Старый способ, совместим со старыми браузерами. Используем для быстрого прототипирования, но лучше addEventListener.
button.onclick = function () {
    picture.remove(); // Удаляем картинку
}

/* Работа с CSS-классами */
/* Методы работы с атрибутами
getAttribute(attrName) - возвращает значение указанного атрибута
setAttribute(name, value) - добавляет указанный атрибут и его значени к элементу
hasAttribute(attrName) - возвращает true при наличии у элемента указанного атрибута
removeAttribute(attrName) - удаляет указанный атрибут
toggleAttribute(name, force) - добавляет новый атрибут при отсутствии или удаляет существующий атрибут. 
-- force true - атрибут гарантированно добавляется, даже если уже есть;
-- force false - атрибут гарантированно удаляется, даже если его не было.

hasAttributes() - возвращает true, если у элемента есть какие-либо атрибуты
getAttributeNames() - возвращает названия атрибутов элемента
*/

const picture = document.getElementById('picture');
picture.getAttribute('src'); // lead.jpg
picture.setAttribute('src', '4c.jpg'); // Заменяем картинку
picture.setAttribute('alt', 'newAlt'); // alt='newAlt'
picture.removeAttribute('alt');
picture.toggleAttribute('alt');

console.log(picture.hasAttribute('alt'));
console.log(picture.hasAttributes());
console.log(picture.getAttributeNames()); // ['src', 'id', 'alt']


picture.setAttribute('src', '4c.jpg');
picture.setAttribute('width', '400');
picture.setAttribute('height', '350');
picture.src = 'lead.jpg'; // Альтернативный способ заменить изображение


/* Проверка содержимого класса */
const heading = document.querySelector('h2');
heading.classList.toggle('red-text');

 // Через переменную
const result2 = heading.classList.contains('red-text') ? 'Класс red-text есть!' : 'Класса red-text нет!';
console.log(result2);

// Напрямую в консоли
console.log(
    heading.classList.contains('red-text') ? 'Класс red-text есть!' : 'Класса red-text нет!'
);

// Стандартно через условия
if (heading.classList.contains('red-text')) {
    console.log('Класс red-text есть!');
} else {
    console.log('Класса red-text нет!');
}


/* Переключение класса (toggle)
const heading = document.querySelector('h2');
heading.classList.toggle('green-text'); // Добавляет класс
console.log(heading.className);
console.log(heading);

heading.classList.toggle('green-text'); // Удаляет класс
console.log(heading.className);
console.log(heading);
*/

/* Добавление/Удаление класса 
const heading = document.querySelector('h2');
heading.classList.add('red-text');
console.log('После добавления:', heading.classList.contains('red-text')); // true
console.log(heading.className); // red-text
console.log(heading);

heading.classList.remove('red-text');
console.log('После удаления:', heading.classList.contains('red-text')); // false
console.log(heading.className);
console.log(heading);


// Выбор одного элемента по DOM-селектору. querySelector возвращает первый найденный на странице элемент
// Можно передавать теги и вложенные классы
const firstElement = document.querySelector('.school-name');
const h2Element = document.querySelector('h2');
console.log(firstElement, h2Element);

// Добавить класс к элементу
const h4 = document.querySelector('h4');
h4.classList.add('red');
console.log(h4);

/* Методы classList 
add
remove
toggle
contains
replace
item(index) - возвращает класс по индексу
*/

// Выбор коллекции элементов
const headings = document.querySelectorAll('h2');

// Добавляем класс к коллекции элементов
headings.forEach(item => {
    item.classList.add('red-text');
    // console.log(item);
});

for (let heading of headings) {
    heading.classList.add('red-text');
    // console.log(element);
}

// Методы старого стандарта
document.getElementById('');
document.getElementsByClassName(''); // Не поддерживает forEach без явного преобразования
document.getElementsByTagName('');




/* Сжать теги html-документа для просмотра структуры: ctrl + K; ctrl + 0 
Вернуть исходное состояние: ctrl + K; ctrl + J */

/* Классы. Конструкторы объектов
Класс - это как чертёж для все будущих объектов, которые будут создаваться на его основе */

class Person {
    // Конструктор (функция, создающая объект и наполняющая его данными - свойствами)
    constructor (userName, age, isMarried) {
        this.userName = userName;
        this.age = age;
        this.isMarried = isMarried;
    }

    // Когда описываем метод в классе, мы не пишем function
    sayHi() {
        console.log(`Привет! Я ${this.userName}.`);
    }
}

const user1 = new Person('Марк', 30, false); // В константу user1 будет записан объект класса Person
const user2 = new Person('Игорь', 28, true); 
console.log(user1, user2, user1.sayHi);
user1.sayHi();
user2.sayHi();



/* Объекты: обход циклом for in 
В отличие от for of, for in может обходить неитерируемые объекты и возвращать ключи */
const persona = {
    userName: 'Марк',
    age: 30,
    isMarried: false,
    sayHi: function(yourName){
        console.log(`Привет, ${yourName}. Меня зовут ${this.userName}`)
    },
};

for (let key in persona) {
    console.log(key);
}


/* Ключевое слово this 
Ключевое слово this внутри метода объекта ссылается на объект */

person1 = {
    userName: 'Igor',
    age: 28,
    isMarried: false,
    // Метод объекта (Свойство, если функция - то это метод)
    sayHi: function(name){
        console.log(`Привет, ${name}! Меня зовут ${this.userName}`);
        // this.userName тоже самое, что person.userName
    }
}

person1.sayHi('Марк');

/* Если используем this внутри функции, которая не является методом объекта (даже если она лежит в методе объекта, но не является методом),
то this будет  терять контекст и ссылаться на глобальный объект window */
function showThis(){
    console.log(this); 
}
showThis(); // window (или undefined, если включен 'use strict')


/* Объекты */
let propertyName = 'Designer';
let hobbyName = 'hobby';

person = {
    userName: 'Igor',
    age: 28,
    isMarried: false,
    profession: propertyName, // Свойство как переменная
    hobby: 'Programming',    // Метод объекта (Свойство, если функция - то это метод)
    sayHi: function(){
        console.log('Привет!');
    },
    'first name': 'Egor'
}

console.log(person.profession);
console.log(person[hobbyName]); // Вызов свойства как переменной
console.log(person.userName); // Используем для простых ключей
console.log(person['age']); // Ключи с пробелами, спецсимволами или является переменной
console.log(person['first name']);


/* Методы объектов */

//  Создаём свойство объекта
person.money = 130000;
console.log(person['money']);

// Удаляем свойство
delete person.age;

// Вызов метода
person.sayHi();

// Создание метода
person.sayBye = (name) => console.log(`Пока, ${name}!`);
person.sayBye('Gregory');



/* Обход массивов */
const autoBrands = ['Audi', 'BMW', 'Mazda', 'Toyota', 'Nissan'];

/* Обход массива с forEach */
autoBrands.forEach(function(item, index){
    console.log(`${index} => ${item}`);
})

// С передачей функции как параметра (вызов функции не нужен)
autoBrands.forEach(printBrand);
function printBrand (brand, i) {
    console.log(`${i} => ${brand}`);
}

// Стрелочная функция
autoBrands.forEach((brand, i) => console.log(`${brand} => ${i}`));


/* Обход массива циклом for ( of ) */

// Массив будет пройден столько раз, сколько в нём элементов
for (let brand of autoBrands) {
    // console.log(brand);
}



/* Методы массивов 
.push() - добавляем элемент в конец массива
.pop() - удалить элемент с конца массива
.shift() - удалить элемент из начала массива
.unshift() - добавить элемент в начало массива
.splice([start], [deleteCount, newElements]); start - с какого индекса стартовать
.slice()
.forEach()
.indexOf()
.includes()
*/
const arr = [['Honda', 'Kia'], 'Audi', 'BMW', 'Nissan', 'Toyota'];
const arr0 = [['Honda', 'Kia'], 'Audi', 'BMW', 'Nissan', 'Toyota'];

console.log(arr == arr0); // false (разные объекты в памяти)
console.log(JSON.stringify(arr) == JSON.stringify(arr0)); // true (значения равны)
// `JSON.stringify` сериализует массив в строку. Работает для примитивов и простых объектов


// Разница в использовании const и let
// 1. const
const arr1 = [1, 2, 3];
arr1.push(4); // ОК: arr = [1, 2, 3, 4]
arr1[0] = 10; // ОК: arr = [10, 2, 3, 4]
// arr = [5, 6, 7]; // Ошибка TypeError (нельзя перезаписывать)

// 2. let: можно переприсвоить
let arr2 = [1, 2, 3];
arr2 = [5, 6, 7]; // ОК: arr2 теперь новый массив

// Метод splice
arr.splice(2, 1);



/* Массивы (коллекции элементов). Имеют индексы */

let arr9 = [['Honda', 'Kia'], 'Audi', 'BMW', 'Nissan', 'Toyota'];
console.log(arr9[0][1]);


/* Стрелочные функции (arrow functions). 
Не имеют свой контекст (this), arguments и super и new, + заимствует (ссылается) на контекст области, в которой она была объявлена 
Часто используется в массивах. */

const arrSayHi = (name) => console.log(`Привет, ${name}! Как твои дела?`);
arrSayHi('igor');

// 1. this. В стрелочных функциях this берётся из внешней области (не из объекта, где функция вызвана). Это полезно в коллбэках, 
// но может быть проблемой в методах объектов.
const obj = {
    name: 'Alice',
    greet: function() { setTimeout(() => console.log(this.name), 1000); }, // Alice
    badGreet: function() { setTimeout(function() { console.log(this.name); }, 1000); } // undefined
}
obj.greet(); // Alice
obj.badGreet(); // undefined

// 2. `arguments`: нет объекта arguments, используйте rest-параметры (`...args`)
// `(a, b, ...rest) => rest` (вместо arguments)
// 3. `super`: не имеют собственного `super`, наследуют из внешнего контекста.
// 4. `new`: нельзя использовать как конструкторы (вызов `new ArrowFunc()` вызовет ошибку)
// 5. Прототип. Нет свойства `prototype`, так что не подходят для классов и наследования.



/* Самовызывающаяся функция IIFE (Immediately Invoked Function Expression) 
- Незамедлительно вызывающееся функциональное выражение. Или анонимная функция.
Обязательно нужна точка с запятой после вызова (), иначе будет ошибка */

(function sayHi() {
    console.log('Привет, дорогой пользователь!');
})();

// С передачей аргументов
(function summ(a, b){
    console.log(a + b);
})(10, 20);


// Вызов с переменной
let res = (function(a, b) {
    return a + b;
})('Igor', ' Oshust');
console.log(res);

/*
IIFE Полезны (в основном до ES6, встречаются в legacy): 
1. Изоляция переменных и предотвращение загрязнения глобального пространства (актуально до ES6)
Например, в старом коде для библиотеки, что не перезаписывать глобальные переменные
2. Модуляция кода: IIFE можно использовать для создания модулей, возвращая объект с публичными методами, скрывая внутреннюю реализацию (актуально до ES6) 
3. Обработка асинхронного кода или циклов
4. Инициализация кода при загрузке страницы */

// Модуляция кода
const myModule = (function() {
    let privateVar = 'secret';
    return {
        publicMethod: () => console.log(privateVar)
    };
})();






/* Коллбек - функция, вызываемая внутри другой функции (функции обратного вызова) */
function summ(a, b){
    return a + b;
}

function diff(a, b){
    return a - b;
}

function doSomething(func){
    let x = 10;
    let y = 15;
    let result = func(x, y); // Коллбек - функция, вызываемая внутри другой функции (функция обратного вызова)
    console.log(result);
}

doSomething(summ);
doSomething(diff); 

// Мой вариант
function summ(a, b) { return a + b }
function diff(a, b) { return a - b }
function doSomething(a, b, func) { return func(a, b) }

console.log(doSomething(20, 30, summ));


/* Функции как параметры */
function summ(a, b){
    return a + b;
}

const result = summ(summ(15, 15), summ(20, 20));

console.log(
    result
);


/* Пример итерации по объекту (Symbol не участвует) */
const id = Symbol();

let my_object = {
    [id]: 12,
    'name': 'Igor'
}

for (let key in my_object) {
    console.log(`Ключ: ${key}, Значение: ${my_object[key]}`);
}

/* Условный оператор */
const time = 20;

if (time < 12) {
    console.log('Доброе утро!');
} else if (time >= 12 && time < 18) {
    console.log('Добрый день');
} else {
    console.log('Добрый вечер');
}

/*Тернарный оператор */
// (условие) ? (условие верно) : (условие не верно);