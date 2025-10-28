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