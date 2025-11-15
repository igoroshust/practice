/*  1. Таймер
    1.1 setTimeout(), setInterval() - скрипт ждёт 2 секунды, считает до 5, заканчивает выполнение
    2. Получение данных по API
    3. Курсы валют
    4. Промисы
    5. Коллбэки
    6. show-hide block
    7. Аккордеон
    8. Табы
    9. Модальное окно 
    10. Повторение теории
*/






/* Пример работы со временем */
/* Мой вариант */
// let counter = 1;
// let timerID;

// setTimeout(() => {

//     timerID = setInterval(() => {
//     console.log(counter);
//     counter++;
//     }, 1000); // 2. Выводим каждую секунду новое значение

//     setTimeout(function(){
//         clearInterval(timerID);
//     }, 10000); // 3. Через 10 секунд прекращаем выполнение

// }, 3000); // 1. Отложенный запуск скрипта через 3 секунды


/* Вариант-1. Инкапсуляция логики в замыкании */

// function createCounter(delay, interval, duration) {
//     let counter = 1;
//     let timerID;

//     setTimeout(() => {
//         timerID = setInterval(() => {
//             console.log(counter);
//             counter++;
//         }, interval);

//         setTimeout(() => clearInterval(timerID), duration);
//     }, delay);
// };

// createCounter(3000, 1000, 10000);


/* Вариант-2. Класс-ориентированный подход */
// class Counter {
//     constructor(delay = 3000, interval = 1000, duration = 10000) {
//         this.counter = 1;
//         this.timerID = null;
//         this.delay = delay;
//         this.interval = interval;
//         this.duration = duration;
//     }

//     start() {
//         setTimeout(() => {
//             this.timerID = setInterval(() => {
//                 console.log(this.counter);
//                 this.counter++;
//             }, this.interval);

//             setTimeout(() => this.stop(), this.duration);
//         }, this.delay);
//     }

//     stop() {
//         clearInterval(this.timerID);
//     }
// }

// // Использование
// const counter = new Counter();
// counter.start();


/* Вариант-3. Promise-based решение */
// function delayedCounter(delay = 3000, interval = 1000, duration = 10000) {
//     return new Promise((resolve) => {
//         let counter = 1;
//         let intervalID, timeoutID;

//         setTimeout(() => {
//             intervalID = setInterval(() => console.log(counter++), interval);
//             timeoutID = setTimeout(() => {
//                 clearInterval(intervalID);
//                 resolve();
//             }, duration);
//         }, delay);
//     });
// };

// // Использование
// delayedCounter().then(() => console.log('Counter finished'));




const city = document.querySelector('.city');
const region = document.querySelector('.region');
const country = document.querySelector('.country');

const apiInfo = fetch('https://ipinfo.io/161.185.160.93/geo')
.then(response => response.json())
.then(data => {

    /* Моя вставка */
    // city.innerText = city.textContent + ' ' + data['city'];
    // region.innerText = region.textContent + ' ' + data['region'];
    // country.innerText = country.textContent + ' ' + data['country'];

    /* Через textContent (Быстрее, чем innerText) */
    // city.textContent += data['city'];

    /* appendChild (+нет перезаписи содержимого, безопасно. -требует создания узла, что немного более многословно.) */
    //city.appendChild(document.createTextNode(' ' + data['city']));
    // Метод document.createTextNode() создаёт текстовый узел (не HTML-элемент!) с указанным текстом (возвращает объект типа Text)
    // Метод appendChild() добавляет узел (элемент или текстовый узел) в конец указанного родительского элемента (в качестве последнего дочернего узла)
    // Сигнатура appendChild: parentElement.appendChild(childNode);

    // Метод insertAdjacentText() позволяет вставлять текст в конкретную позицию относительно элемента
    // +быстрый +не требует создания узлов + гибкий -менее известный метод -возможно не поддерживается в старых браузерах
    // city.insertAdjacentText('beforeend', ' ' + data['city']);

    // Использование шаблонных строк или циклов для нескольких элементов
    
})
.catch(error => {
    console.error(error);
})


/* document.createTextNode() - метод оздания текстового узла на странице.
Позволяет безопасно добавлять текст, любой переданный текст воспринимается как текст, а не HTML, что защищает от XSS-уязвимостей */

// Опасный способ (может выполнить скрипт!)
// city.innerHTML = alert("<script>alert('Взлом!')</script>");

// // Безопасный способ
// const text = document.createTextNode('<script>alert("Не сработает!");</script>');
// city.appendChild(text);


/* XSS (Cross-Site scripting, межсайтовый скриптинг) - это уязвимость веб-приложений, позволяющая злоумышленнику внедрить и выполнить вредоносный код (обычно, JS) 
в контексте доверенного сайта, который просматривает жертва. */

/* Кейс: вывести данные API через forEach */
const elements = [
    { selector: '.city', key: 'city' },
    { selector: '.region', key: 'region' },
    { selector: '.country', key: 'country' },
    { selector: '.ip', key: 'ip' },
    { selector: '.timezone', key: 'timezone' },
];

const apiInfo1 = fetch('https://ipinfo.io/161.185.160.93/geo')
.then(response => response.json())
.then(data => {

    console.log(data);

    elements.forEach(({ selector, key }) => {
        // Деструктуризация { selector, key } извлекает свойства из каждого объекта. Позволяет распаковать свойства объекта прямо в переменные внутри параметрой функции.
        // Здесь selector и key уже доступны как переменные
        const el = document.querySelector(selector);
        el.textContent += data[key];

        // Аналог записи без деструктуризации
        // elements.forEach(item => {
        //     const selector = item.selector;
        //     const key = item.key;
        // })

        // Вариант с текстовым узлом
        //     elements.forEach(({ selector, key }) => {
        //     item = document.querySelector(selector);
        //     node = document.createTextNode(data[key]);
        //     item.appendChild(node);
        // })
    })
})
.catch(error => {
    console.error(error);
})


/* Пример деструктуризации */
const obj = { selector: '.city', key: 'city'};
const { selector, key } = obj;

console.log(selector); // .city
console.log(key); // city