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