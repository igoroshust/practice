# Темы для разбора:
- Поднятие (hoisting);
- Сферы применения ЯП (когда лучше использовать один, когда - другой);
- this
- Замыкания
- Функции высшего порядка
- Выражения, инструкции
- Принцип определения объёма необходимой памяти
- Метрики оценки качества веб-приложения
- Тестирование во фронтенде
- Использование постман
- SASS, LESS, SCSS
- jQuery


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