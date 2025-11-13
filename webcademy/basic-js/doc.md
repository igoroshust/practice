# Темы для разбора:
- event 
- target
- Событийная модель JavaScript (DOM Events -- event, target, etc.)
- defer

- classList
- FETCH API
- DOM API
- DOMTokenList
- Поднятие (hoisting)
- Полифилы
- Сферы применения ЯП (когда лучше использовать один, когда - другой);
- this
- throw
- ; - подробнее о назначении точки с запятой
- Замыкания
- XMLHttpRequest
- Server-Side Rendering
- Функции высшего порядка
- Выражения, инструкции
- Принцип определения объёма необходимой памяти
- Метрики оценки качества веб-приложения
- Тестирование во фронтенде
- Использование постман
- SASS, LESS, SCSS
- jQuery
- document
- querySelector
-  Airbnb JS Style Guide


### event, target, event.target
event, target, event.target - это концепции из событийной модели JavaScipt (DOM Events). Когда происходит событие (например, клик), браузер создаёт объект `event` и передаёт его в обработчик функции.

- `event`: Это объект события (типа `MouseEvent` или `Event`). Он содержит информацию о событии: координаты, тип, время и т.д. В коде `addEventListener('click', (event) => { ... })` event - это параметр, который можно назвать как угодно (например, `e`). event - объект, содержащий информацию по конкретному событию.

- `target`: Это свойство объекта event. Оно указывает на DOM-элемент, который вызвал событие (на котором произошёл клик). Если кликнули на `<li>`, `event-target` - это тот `<li>`.

- `event.target`: Полный доступ к элементу-источнику. Может быть использован для проверки, что клик был именно по целевому элементу, а не на пустом месте.


**Пример**
```javascript
tabList.addEventListener('click', (event) => {
    console.log(event.target); // Выведет элемент, на который кликнули (например, <li>)
    console.log(event.type); // 'click'
})
```




### className
`className` - это свойство DOM-элемента в JS, которое напрямую соответствует атрибуту `class` в HTML. Оно представляет все CSS-классы элемента как единую строку, разделённую пробелами. Это часть DOM API и работает во всех браузерах, включая старые.

**Как работает?**
- Чтение: возвращает строку с классами. Для `<div class="card active">` -> `element.className` вернёт `"card active"`.
- Запись: полностью заменяет строку классов. `element.className = "new-class hidden"` - старые классы удаляются, новые добавляются.
- Тип: всегда строка. Если классов нет, возвращает пустую строку `""`.
- Синхронизация: Изменения в `className` сразу отображаются в HTML и наоборот.

**Пример использования**
```javascript
const div = document.querySelector('#myDiv');

// Чтение классов
console.log(div.className); // "card active"

// Добавление класса (ручное, с пробелом)
div.className += ' hidden';

// Замена всех классов
div.className = "error"; // Теперь только "error"

// Удаление класса (ручное, с заменой)
div.className = div.className.replace("error", "").trim(); // Удалит "error", уберёт лишний пробел
```

**Отображение в браузере наглядно**
```javascript
let show = document.querySelector('#button');
undefined
show.className;
'hadsas'
```

**Сравнение с classList**
`classList` (рекомендуется для манипуляций):
    - Имеет методы `add()`, `remove()`, `toggle()`, `contains()`
    - Удобен для отдельных классов, предотвращает дубликаты и ошибки с пробелами;
    `div.classList.add('active') - добавляет класс без замены других

`className`
    - Простая строка, но требует ручной работы с пробелами (например, `+= "class"` создать дубликаты или лишние пробелы);
    - Лучше для полной замены или чтения всех классов сразу.
    - В старых браузерах (до IE10) `classList` не поддерживается, так что `className` - альтернатива.


**Когда использовать className?**
- Для полной замены классов: когда нужно сбросить всё и установить новые (например, в циклах или при переключении состояний);
- Для чтения/парсинга: если нужно обработать все классы как строку (например, с `split()` или регулярками).
- В старых браузерах: где `classList` недоступен.
- Не использовать: для частых добавлений/удалений - лучше `classList` для избежания ошибок.

**Недостатки**
- Ручная работа с пробелами: легко добавить дубликаты (например, `className += "active"` может дать `"card active active"`)
- Менее безопасно: ошибки в строке ломают стили (лишние пробелы или отсутствие пробелов)
- Неудобно для динамики: для toggle или проверки лучше `classList`.



### classList
`classList` - свойство DOM-элемента в JS, предоставляющее удобный интерфейс для работы с CSS-классами элемента. Оно представляет собой объект типа `DOMTokenList` (список токенов), содержащий все классы элемента как массивоподобную структуру. Это часть стандарта HTML5 и работает во всех современных браузерах.

**Пример использования**
```javascript
const div = document.querySelector('#myDiv');

// Добавляем классы
div.classList.add('card', 'active');

// Переключаем класс
div.classList.toggle('hidden'); // Добавит 'hidden', если его нет

// Проверяем и удаляем
if (div.classList.contains('active')) {
    div.classList.remove('active');
}

// Результат: <div id="myDiv" class="card hidden"></div>
```

**Как это работает?**
- `classList` автоматически синхронизируется с атрибутом `class` элемента. Изменения через `classList` сразу отражаются в HTML.
- Доступ: `element.classList` (`document.querySelector('.my-div').classList`).
- Классы хранятся как строки, разделённые пробелами, но `classList` позволяет манипулировать ими по отдельности.

**Основные методы**
- add
- remove
- toggle
- contains
- replace
- length
- item

**Когда использовать**
- Рекомендуется: для динамического управления классами в интерактивных приложениях (показ/скрытие элементов, анимация). Лучше ручного изменения `element.className` (строки), так как `classList` предотвращает ошибки с пробелами и дубликатами.
- Не использовать: если нужно работать со всей строкой классов (тогда `element.className`).
- Поддержка: Работает с IE10+; для старых браузеров нужно использовать полифилы.

**classList наглядно в браузере**
```javascript
let show = document.querySelector('#button');

> show.classList
< DOMTokenList(3) ['btn', 'btn-outline-primary', 'mb-3', value: 'btn btn-outline-primary mb-3']0: "btn"1: "btn-outline-primary"2: "mb-3"length: 3value: "btn btn-outline-primary mb-3"[[Prototype]]: DOMTokenList
```


**Дополнительно**
- DOM-элемент - это объект в JS, представляющий HTML-тег в документе (например, `<div>` или `<button>`). Он позволяет программно манипулировать структурой, стилем, содержимым и поведением страницы через API DOM.

- DOMTokenList - интерфейс для работы со списками разделённых пробелами значений (токенов), таких как CSS-классы. Он используется в `classList` для удобного добавления, удаления и проверки классов, обеспечивая автоматическую синхронизацию с атрибутом `class` и предотвращая ошибки с пробелами/дубликатами.

- Полифилы - это JS-библиотеки или скрипты, которые добавляют поддержку современных функций (например, `classList` или `fetch`) в старых браузерах, где они отсутствуют, эмулируя их поведение.


### function declaration и function expression

**function declaration** (можно вызывать до объявления функции)
```javascript
console.log(calculateSum(10, 20)); // 30
function calculateSum(x, y) {
    let result = x + y;
    return result;
};
console.log(calculateSum(10, 20)); // 30
```


**function expression** (нельзя вызвать до объявления функции)
```javascript
console.log(calculateSumma(10, 20)); // Ошибка: uncaught ReferenceError: Cannot access 'calculateSumma' before initialization
const calculateSumma = (x, y) => x + y;
console.log(calculateSumma(10, 20)); // 30

// Аналог записи FE
const calculate = function(x, y) {
    // Код...
}
```

### Массивы
Способ группировки данных, при котором данные объединяются в одну коллекцию. Подходят для значений, объединённых между собой по смыслу.
```javascript
const fruits = ["Яблоко", "Груша", "Слива"];
```

**Метод forEach**
```javascript
const fruits = ["Яблоко", "Груша", "Слива"];
fruits.forEach((item, index) => {
    console.log(`${index} => ${item}`);
});
// Метод forEach принимает cb-функцию с параметрами (значение элемента, индекс)
```

### var, let, const (отличия)

#### var
var имеет **функциональную область видимости**. Это значит, что они доступны в пределах всей функции, где объявлены, включая все вложенные блоки (циклы, условия), но не за пределами функции. Если `var` объявлена вне функции, она становится глобальной переменной. var был введён в неактуальном поныне стандарте ES5, в новых программах следует использовать let и const.

**Пример-1 (внутри функции)**
```javascript
function doSomething(){
    var a = 10;
    if (a) {
        var b = 20;
        let c = 30;
    }
    console.log(b); // 20 (доступна везде внутри функции)
    console.log(c); // ошибка
};

doSomething();
    console.log(b); // ошибка (вне функции b не определена)
    console.log(c); // ошибка
```

**Пример-2 (в цикле)**
```javascript
for (var i = 0; i < 3; i++){
    console.log(i); // i доступна здесь (0, 1, 2)
}
console.log(i); // 3 (значение доступно после завершения цикла, что может привести к неожиданным результатам)
```

#### let, const
let и const имеют **блочную область видимости**, что означает видимость переменных только внутри конкретного блока `{}`, включая вложенные блоки, но не снаружи.
`const` отличается от `let` тем, что её значение нельзя переприсвоить после инициализации.

**Пример-1 (внутри функции)**
```javascript
if (true) {
    const a = 10;
    const b = 20;
}
console.log(a); // Ошибка: a не определена
console.log(b); // Ошибка: b не определена
```

**Пример-2 (внутри функции)**
```javascript
if (true) {
    for (let i = 0; i < 3; i++){
        for (let j = 1; j <= 3; j++){
            console.log(i, j); // Корректный вывод
        }
        console.log(j); // Ошибка
        console.log(i); // Корректный вывод
    }
    console.log(i); // Ошибка
};
```

**Пример-3 (внутри цикла)**
```javascript
for (let j = 0; j < 3; j++){
    console.log(j); // j доступна только здесь
}
console.log(j); // Ошибка: j не определена (предотвращает утечку переменной и делает код более предсказуемым)
```

**Пример-4 (внутри вложенного блока)**
```javascript
function test(){
    var x = 1; // Функциональная видимость
    if (true) {
        let y = 2; // Блочная видимость
        console.log(x); // 1 (x доступна)
        console.log(y); // 2 (y доступна)
    }
    console.log(x); // 1 (x доступна)
    console.log(y); // Ошибка (y недоступна)
}
test();
```

#### Ключевые отличия
- Изоляция. `let/const` предотвращают случайное переопределение переменных в разных блоках (например, циклах или условиях), что снижает ошибки. `var` может перезаписывать себя в разных частях программы.
- Глобальная видимость. `var` вне функции может загрязнять глобальное пространство, `let/const` всегда ограничены блоком.
- Поднятие (hoisting). `var` поднимается в начало функции (можно использовать до объявления, но со значением `undefined`). `let/const` тоже поднимаются, но в "мёртвой зоне" (ошибка при доступе до объявления).
- Рекомендации. `let` для изменяемых переменных, `const` для констант. `var` устарел и может привести к багам в сложном коде (например, в асинхронных функциях или модулях).


#### Пример различия функциональной и блочной областей видимости
```javascript
{
    var test1 = 'test1';
    let test2 = 'asddas';
    const test3 = 'qwerty';
}

console.log(test1); // test1
console.log(test2); // ошибка
console.log(test3); // ошибка
```


### data-атрибуты (html)
Data-атрибуты (data attributes) - это специальные атрибуты в HTML, позволяющие хранить дополнительные данные прямо в элементах DOM. Они начинаются с `data-` и могут содержать любую строку (`data-user-id="123"`, `data-tooltip="Подсказка"` и т.д.). Эти атрибуты не влияют на стандартное поведение браузера или CSS, но доступны для JavaScript. Это своего рода кармашек для данных в DOM-элементах.

Дата-атрибуты созданы для хранения информации, с их помощью можно идентифицировать элементы. Они имеют непосредственное отношение к данным, скриптам, подходят для идентификации нескольких связанных объектов (например, при реализации аккордеона для выявления связанных элементов с целью повесить обработчик события по клику);

Ещё они важны для решения проблемы с изменением классов. Если класс изменится, то придётся скрипт переделывать, а вот дата-атрибут не зависит от класса, поэтому он остаётся статичным. Классы больше ориентированы на стилизацию, **в то время как data-атрибуты предназначены для JS, а не для стилей**.

data-атрибуты могут не иметь значения (и это не будет ошибкой):
```html
<div class="card p-3 hidden" data-tab-content id="tab-1">
```

**Использование в HTML**
```html
<button data-action-example="save" data-value-example="42">Отправить</button>
```

**Обработка в JS**
```javascript
const button = document.querySelector('button');
console.log(button.dataset.actionExample); // "save"
console.log(button.dataset.valueExample); // "42"
```

#### Зачем нужны data-атрибуты?
- Хранение метаданных. Позволяют прикреплять данные к элементам без изменения структуры HTML или использования глобальных переменных. Это полезно для динамического контента, где данные приходят из JS или сервера.
- Изоляция данных. Избегают смешивания логики с HTML (например, вместо хранения текста в JS, храните его в data-атрибуте для гибкости).
- Доступность и поддерживаемость. Упрощают код, делая его более декларативным. Например, вместо хардкода в JS можно читать данные из HTML, что упрощает изменения.
- SEO и валидность. Не ломают HTML-стандарты и игнорируются поисковиками/валидаторами.


#### Когда нужны data-атрибуты?
- Для динамических данных. Когда элементам нужно хранить состояние или конфигурацию (например, ID пользователя, настройка виджета).
- В интерактивных приложениях. Для тултипов, модальных окон, форм.
- При локализации или конфигурации. Хранить тексты, URL или параметры в HTML, чтобы JS обрабатывал их оттуда.
- **НЕ ИСПОЛЬЗОВАТЬ, ЕСЛИ**. Данные лучше хранить в JS (сложные объекты) или если атрибуты делают HTML перегруженным. Для больших объёмов данных предпочтительнее JSON или API.


#### dataset - принцип работы
`dataset` - свойство DOM-элемента в JavaScript (стандарт HTML5), которое предоставляет доступ ко всем data-атрибутам элемента как к объекту. Оно автоматически преобразует data-атрибуты в свойства объекта. Для data-атрибутов лучше работать с ним, чем через getAttribute (он больше подходит для других атрибутов и старых браузеров)

- `dataset` - это объект (типа `DOMStringMap`), где ключи - это имена data-атрибутов без префиксов `data-`, а значения - строки из атрибутов.

**Пример (HTML)**
```html
<div data-user-name="John" data-age="30"></div>
```

**Обработка (JS)**
```javascript
const div = document.querySelector('div');
console.log(div.dataset); // { userName: "John", age: "30" }
```

#### Важные нюансы работы dataset
- JS автоматически убирает префикс `data-` и преобразует kebab-case в camelCase (`data-open-text` => `openText`).

**Практический пример использования (открыть/скрыть блок)**
```html
    <h1 class="mb-4">Скрыть/Открыть блок</h1>

    <button class="btn btn-outline-primary mb-3" id="button" type="button" data-open-text="Открыть блок" data-close-text="Закрыть блок">
        Открыть блок
    </button>

    <div class="card card-body content-hidden" id="content">
        Блок с контентом. Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quos amet illum molestias qui accusantium saepe doloribus voluptate modi unde, eaque dicta velit voluptatibus 
        cupiditate, maiores similique odit veritatis, animi tempora?
    </div>
```

```javascript
/* Получение значений из дата-атрибутов для кнопки */
const blockContent = document.querySelector('#content');
const btnOpen = document.querySelector('#button');

const openText = btnOpen.dataset.openText;
const closeText = btnOpen.dataset.closeText;

// const openText = btnOpen.getAttribute('data-open-text');
// const closedText = btnOpen.getAttribute('data-closed-text');

btnOpen.addEventListener('click', () => {
    blockContent.classList.toggle('content-hidden');
    btnOpen.innerText = blockContent.classList.contains('content-hidden') ? openText : closeText;
});
```

### DOM API
DOM API (Document Object Model Application Programming Interface) - это набор методов и свойств в JavaScript для программного взаимодействия с HTML/XML-документами. Позволяет создавать, изменять, удалять элементы, атрибуты, стили и обрабатывать события. Пример: `document.querySelector()`, `element.classList.add()`. Это основа для динамических веб-страниц.


### FETCH API
FETCH API - это современный интерфейс в JavaScript для выполнения HTTP-запросов (GET, POST и т.д.) к серверу. Заменяет старый XMLHttpRequest, возвращает Promise. Пример: `fetch('url').then(reponse => response.json())`. Поддерживается в современных браузерах, для старых - полифилы.

### Emmet быстрая запись (принцип)
```html
list-group-item[value="igor"][name="test"]{Test 3}*5
<!-- 
 [] указывает свойство со значениями
 {} устанавливает значение тега
-->
```

Получается
```html
    <list-group-item value="igor" name="test">Test 3</list-group-item>
    <list-group-item value="igor" name="test">Test 3</list-group-item>
    <list-group-item value="igor" name="test">Test 3</list-group-item>
    <list-group-item value="igor" name="test">Test 3</list-group-item>
    <list-group-item value="igor" name="test">Test 3</list-group-item>
```

**Если нужно инкрементировать число (c 1)**
```html
li.list-group-item[data-tab="tab-$"]{Test $}*4
```

**Инкремент с другого числа**
```html
li.list-group-item[data-tab="tab-$@5"]{Test $@5}*4
```