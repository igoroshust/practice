/* Коллбэеки
Коллбэк - функция, передаваемая в качестве аргумента другой функции и должна быть выполнена после завершения раоты этой функции. 
Функция, принимающая другую функцию в качестве аргумента, называется функцией высшего порядка. Переданная ей функция и есть коллбек.*/

// Пример callback
function greet(name, callback) {
    console.log(`Привет, ${name}!`);
    callback(); // Вызываем коллбек после вывода приветствия
}

function sayGoodbye() {
    console.log(`Пока!`);
}

greet('Алиса', sayGoodbye); // Вызываем greet, передавая sayGoodbye как коллбэк


/* Вывод значений параметров функции высшего порядка внутри callback */

// Первый способ. Замыкание
// Передаём в greet не саму функцию sayGoodbye, а анонимную функцию-обёртку, которая запомнит имя через замыкание:
function greet0(name, callback) {
    console.log(`Привет, ${name}!`);
    callback(); // Вызываем коллбек после вывода приветствия
}
function sayGoodbye(name) {
    console.log(`Пока, ${name}!`);
}
// Создаём обёртку, которая "захватит" name
greet0('Алиса', function(){
    sayGoodbye('Алиса'); // Анонимная функция помнит значение благодаря механизму замыканий и передаёт его в sayGoodbye при вызове
});

// Второй способ. Каррирование (создаём функцию-генератор, возвращающую коллбэк с зашитым именем)
// Плюсы: переиспользуемость (можно создавать коллбэки для разных имён) + чистота: основной коллбэк (createGoodbyeCallback) не зависит от внешних переменных
function greet1(name, callback){
    console.log(`Привет, ${name}!`);
    callback();
};
function createGoodbyeCallback(name){
    return function(){
        console.log(`Пока, ${name}!`)
    };
};
greet1('Алиса', createGoodbyeCallback('Алиса'));

// Третий способ. Привязка контекста, используя bind (привязываем имя к функции через function.prototype.bind)
function greet2(name, callback){
    console.log(`Привет, ${name}!`);
    callback();
};
function sayGoodbye(){
    // this здесь будет объектом, к которому привязано имя
    console.log(`Пока, ${this.name}`);
};
// Привязываем имя к контексту функции (this внутри sayGoodbye будет объектом { name: 'Алиса' }). Подходит, если нужно передать несколько данных (не только имя)
greet2('Алиса', sayGoodbye.bind({ name: 'Алиса' })); 

/* Асинхронность - это возможность выполнять несколько задач параллельно или с перекрытием, не дожидаясь завершения каждой из задач. 
- Операции могут стартовать, выполняться и завершаться независимо. 
- Код не блокируется на долгих операциях, 
- Система может обрабатывать другие задачи, пока дожидается результата 

Синхронность - это строго последовательное выполнение кода, при котором каждая следующая операция ждёт завершения предыдущей.
- Программа выполняется шаг за шагом;
- Пока одна задача не завершится, следующая не начнётся;
- Если функция выполняет чтение файла, весь код "замораживается" до окончания чтения. */

// Callback. Callback hell

// Последовательный вызов функций (учебный пример)
// setTimeout(() => {
//     console.log('Step 1');
//     setTimeout(() => {
//         console.log('Step 2');
//         setTimeout(() => {
//             console.log('Step 3');
//         }, 1000);
//     }, 1500);
// }, 2000);

/* Коллбек-функции - функции, которые передаются в другие функции и вызываются после их завершения */

// Мой пример проверки номеров
// function checkRooms1(callback){
//     console.log('Проверяем номера в отеле...');
//     const availableRooms = true;
//     setTimeout(function(){
//         callback(availableRooms);
//     }, 3000);
// };
// function checkRoomsResult1(availableRooms) {
//     const result = availableRooms ? 'Номера есть!' : 'Номеров нет.';
//     console.log(result);
// };
// checkRooms1(checkRoomsResult1);

// Первый пример проверки номеров (учитель)
// function checkRooms(){
//     setTimeout(function(){
//         console.log('Проверяем номера в отеле...');
//         const availableRooms = true;
    
//         if (availableRooms) {
//             console.log('Номера есть!');
//             console.log('Едем в отпуск!');
//         } else {
//             console.log('Номеров нет!');
//             console.log('Отпуск отменяется.');
//         }
//     }, 1000);
// };
// checkRooms();


// Второй пример (проверка номеров + билетов)
// function checkRooms(){
//     setTimeout(function(){
//         console.log('Проверяем номера в отеле...');
//         const availableRooms = true;

//         if (availableRooms){
//             let message = 'Номера есть';
//             submitVacation(message);
//         } else {
//             let message = 'Номеров нет';
//             cancelVacation(message);
//         }
//     })
// };
// function cancelVacation(message){
//     console.log('----- cancelVacation -----');
//     console.log('Ответ на предыдущем шаге:', message);
//     console.log('Отпуск отменяется.');
// };
// function submitVacation(message){
//     console.log('----- submitVacation -----');
//     console.log('Ответ на предыдущем шаге:', message);
//     console.log('Едем в отпуск!');
// };
// checkRooms();


// Третий пример (передача коллбеков)
// function checkRooms(success, failed){
//     setTimeout(function(){
//         console.log('Проверяем номера в отеле...');
//         const availableRooms = true;
//         if (availableRooms){
//             let message = 'Номера есть';
//             success(message);
//         } else {
//             let message = 'Номеров нет';
//             failed(message);
//         }
//     })
// };
// checkRooms(submitVacation, cancelVacation);
// function cancelVacation(message){
//     console.log('----- cancelVacation -----');
//     console.log('Ответ на предыдущем шаге:', message);
//     console.log('Отпуск отменяется.');
// };

// function submitVacation(message){
//     console.log('----- submitVacation -----');
//     console.log('Ответ на предыдущем шаге:', message);
//     console.log('Едем в отпуск!');
// };


// Четвёртый пример (проверка билетов)
function checkRooms(success, failed){
    setTimeout(function(){
        console.log('Проверяем номера в отеле...');
        const availableRooms = true;

        if (availableRooms){
            let message = 'Номера есть';
            success(message);
        } else {
            let message = 'Номеров нет';
            failed(message);
        }
    })
};

function checkTickets(message, success, failed){
    setTimeout(function(){
        console.log('----- function checkTickets -----');
        console.log('Ответ на предыдущем шаге:', message);

        console.log('Проверяем авиабилеты...');
        const availableTickets = true;

        if (availableTickets){
            let message = 'Билеты есть';
            success(message);
        } else {
            let message = 'Билетов нет';
            failed(message);
        }
    }, 500);
}

function cancelVacation(message){
    console.log('----- cancelVacation -----');
    console.log('Ответ на предыдущем шаге:', message);
    console.log('Отпуск отменяется.');
};
function submitVacation(message){
    console.log('----- submitVacation -----');
    console.log('Ответ на предыдущем шаге:', message);
    console.log('Едем в отпуск!');
};

// callback hell разростается
// код уезжает вправо

checkRooms(
    // success
    function(messageFromCheckRooms){
        checkTickets(
            messageFromCheckRooms, 
            function(messageFromCheckTickets){
                submitVacation(messageFromCheckTickets);
            },
            function(messageFromCheckTickets){
                cancelVacation(messageFromCheckTickets);
            })
    }, 
    // failed
    function(messageFromCheckRooms){
        cancelVacation(messageFromCheckRooms)
    }
);

/* Более упрощённый вариант вышестоящего кода вызова функции checkRooms
checkRooms(
    function(messageFromCheckRooms){
        checkTickets(
            messageFromCheckRooms,
            submitVacation,
            cancelVacation
        )
    },
    cancelVacation
); 
*/



/* setInterval Позволяет запускать код через определённый промежуток (интервал) времени
setInterval(функция, время запуска); 
setInterval(function(){}, 1000); - выполнение функции каждую секунду 
При запуске setInterval возвращается идентификатор данного интервала (по которому его можно определить и остановить) 
clearInterval() позволяет очистить интервал */

const timerIntervalID = setInterval(function(){ console.log('Fired!'); }, 1000);
clearInterval(timerIntervalID);


/* setTimeout - функция, выполяющая код через определённый промежуток времени 
setTimeout(function(){}, 5000); - код выполнится через 5 секунд 
При запуске возвращается идентификатор таймера (по которому его можно остановить) */

const timerID = setTimeout(function(){ console.log('Fired'); }, 2000);
clearInterval(timerID); 

/* setInterval + setTimeout
Задание (вывести fired 10 секунд, затем остановить вызов) */

const timerIntervalID_1 = setInterval(function(){ console.log('Fired'); }, 1000);

setTimeout(() => {
    clearInterval(timerIntervalID_1);
}, 10000);


/* Выбор DOM-элементов */

// Выбор контейнера
const container = document.querySelector('#elementsContainer');

// Создание заголовка + наполнение контентом
const newHeader = document.createElement('р1');
newHeader.innerText = 'New Header';
container.append(newHeader);

// Копирование шапки
// const mainHeader = document.querySelector('header');
// // const headerCopy = mainHeader.cloneNode(); // Клонирутся только шапка без содержимого (<header></header>)
// const headerCopy = mainHeader.cloneNode(true); // Клонирутся с внутренним содержимым
// container.append(headerCopy);


// Вставка разметки через строки
const htmlExample = '<h2>H2</h2>';
container.insertAdjacentHTML('beforeend', htmlExample);

// Вставка разметки через шаблонные строки
const title = 'Текст заголовка';
const htmlExample1 = `<h2>${title}</h2>`;
container.insertAdjacentHTML('beforeend', htmlExample1);


/* Шпаргалка 
// Создать элемент
document.createElement('');

// Изменить HTML-содержимое внутри элемента
element.innerHTML = '';

// Изменить текстовое содержимое внутри элемента
node.innerText = ''

// Клонирование элемента
node.cloneNode() // true с внутренним содержимым (текст и теги), false - без внутреннего содержимого

// Вставить элемент внутрь другого элемента
element.append(nodesOrDOMStrings)

// Удалить элемент
element.remove()
*/

/* Объект event 
event - объект события, автоматически передаваемый в обработчик события в JS. Он содержит информацию о произошедшем событии (клик, нажатие клавиши, отправка формы и т.д.) */

const list = document.querySelector('#list');

list.addEventListener('click', function (event){
    console.log(this); // Инфо об элементе c id=list
    console.log(event); // Информация о событии
    console.log(event.target); // HTML-элемент, спровоцировавший событие (li, например)
    console.log(event.currentTarget); // Элемент, к которому применён обработчик (ul в данном случае)
});


/* Прослушка событий №2 */
const inputText = document.querySelector('#input-text');
const textBlock = document.querySelector('#text-block');

inputText.addEventListener('input', inputHandler);

function inputHandler (){
    textBlock.innerText = inputText.value;
}


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