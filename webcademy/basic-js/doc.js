/* Функция-конструктор - создание объекта. Смысл: однократное описание структуры с целью дальнейшего переиспользования */

function Person(name, age, speciality, city) {
    this.name = name;
    this.age = age;
    this.spiciality = speciality;
    this.city = city;

    // Создаём функцию, доступную экземплярам вовне
    this.sayHi = function() {
        return `${this.name} says "Hi!"`;
    }

    // Функция создаётся локально внутри метода и недоступна для вызова извне
    function sayGoodbye(personName) {
        return `${personName} says "Goodbye!"`;
    }

    // Пример использования функции внутри метода
    // console.log(sayGoodbye(this.name));
}

const kirill = new Person('kirill', 28, 'web', 'Yakutsk');
// console.log(kirill.sayHi());


/* Пример создания класса (чертежа) с экземплярами */
class Human {
    constructor(name, age, speciality, city) {
        this.name = name;
        this.age = age;
        this.speciality = speciality;
        this.city = city;

        // Первый способ объявить метод (каждая копия метода занимает отдельное место в памяти. Если создать 1000 экземпляров, будет 1000 отдельных функций `sayHi`,
        // что не эффективно для больших объемов данных, но может быть полезно в контексте замыкания)
        this.sayHi = function(){
            return `${this.name} says "Hi!"`
        }
    };

    // Второй способ объявить метод (одна копия метода на весь класс. Для 1000 экземпляров - всего одна функция `sayGoodbye`, 
    // что экономит память и ускоряет создание объектов).

    sayGoodbye() {
        return `${this.name} says "Goodbye!"`
    }
};
const igor = new Human('igor', 28, 'web developer', 'Tchita');

// console.log(igor.sayHi());
// console.log(igor.sayGoodbye());



/* Объекты. Способ группировки информации
Свойство - определённое значение, присвоенное объекту
Метод - способность объекта совершать действие (функция, являющаяся свойством объекта) 
this внутри метода объекта ссылается на сам объект */

const peter = {
    name: 'Peter',
    age: 28,
    spiciality: 'html coder',
    city: 'Moscow',
    sayHi: function(){
        return `${this.name} says "Hi!"`
    }
};

// console.log(peter.sayHi());



/* Пример вызова функции в параметрах другой функции */
function calculateSum(x, y) {
    let result = x + y;
    return result; // 15
}
let res = calculateSum(calculateSum(10, 20), calculateSum(30, 40));
console.log(res);



/* SWITCH CASE. Проверка значения переменной на различные варианты (альтернатива if-else)
    + улучшает читабельность кода при множестве условий 
    switch (выражение) {
        case значение:
            // Код для выполнения, если выражение == значение
            break;
        default:
            // Код, если ни один case не подошёл
            break;
    } 
*/

const mark = 5;

switch (mark){
    case 5:
        console.log('Awesome!');
        break; // Если break не закомментировать, следующий case отработает автоматически
    case 4:
        console.log('Good.');
        break;
    case 3:
        console.log('Neighter good, not bad.');
        break;
    case 2:
        console.log('Bad.');
        break;
    case 1:
        console.log('Terrible.');
        break;
    default:
        console.log('Value out of case.');
        break;
}


/* Пример функции с умножением числа на само себя */

// Метод repeat()
let b = 'b';
let output = b.repeat(3);
console.log(output); // bbb

// Функция (моя)
let a = 'a';

function mult(variable, count){
    let resultValue = variable;

    for (let i = 1; i < count; i++){
        resultValue += variable;
    }
    return resultValue;
}

let result = mult(a, 5);
console.log(result);

/* Пример добавления finally в for */
function example(){
    try {
        for (let i = 0; i < 10; i++) {
            console.log('i = ' + i);
            if (i == 5) break; // Или throw new Error();
        }
    } finally {
        console.log('Это выполнится всегда (finally)');
    }
}
example();


/* Создать новый файл через консоль powershell 
fsutil file createnew "doc.js" 0
0 - размер файла в байтах (пустой) */