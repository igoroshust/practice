/* Выбор одного элемента DOM по селектору */
// document.querySelector('selector');
document.querySelector('h2');

/* Добавить класс элементу */
document.querySelector('h2').classList.add('red');

// Пример
const heading2 = document.querySelector('h2');
heading2.classList.add('red');

/* Выбор коллекции элементов (все элементы с h2) */
const headings = document.querySelectorAll('h2');
console.log(headings);

// Пример
for (let item of headings) {
    item.classList.add('ss');
}

// Присвоение через for of
const paragraphs = document.querySelectorAll('p');
for (let p of paragraphs) {
    p.classList.add('green');
}

// Присвоение через forEach
paragraphs.forEach(function(item){
    item.classList.add('dd');
})


/* Дополнительные методы */
// document.getElementsByClassName(); // Выбор коллекции элементов по CSS-классу
// document.getElementsByTagName(); // Выбор коллекции элементов по тегу
// document.getElementById(); // Выбор одного элемента по ID


/* ============================================= Работа с CSS-классами ============================================== */

/*
element.classList.add()
.add()
.remove()
.toggle() - переключает css-класс (убирает, если был или добавляет, если не было).
.toggle() Возвращает true/false в зависимости от того, был класс добавлен или

.contains() - true/false по наличию/отсутствию класса у элемента
*/

const heading = document.querySelector('h2');
console.log(heading.classList.contains('ss')); // true


/* ===================================== Работа с атрибутами (alt, src и т.д.) ====================================== */

/*
getAttribute(attrName) - возвращает значение указанного атрибута
setAttribute(name, value) - добавляет указанные атрибуты и его значение к элементу
hasAttribute(attrName) - возвращает true при наличии у элемента указанного атрибута
removeAttribute(attrName) - удаляет указанный атрибут

toggleAttribute(name, force) - добавляет новый атрибут при отсутствии или удаляет существующий атрибут
hasAttributes() - возвращает true, если у элемента имеются какие-либо атрибуты
getAttributesName() - возвращает названия атрибутов элемента
*/

// Выводим значение атрибута src
const img = document.querySelector('#logo');
const srcValue = img.getAttribute('src');
console.log(srcValue); // ./js.jpg

// Меняем атрибуты img
img.setAttribute('src', './some.jpg'); // Меняем картинку
img.setAttribute('width', '200'); // Регулируем ширину
img.src = './js.jpg'; // Альтернативный способ записи

// Меняем значение кнопки
const button = document.querySelector('#button');
button.setAttribute('value', 'Отправить');
button.value = "Текст для кнопки";


/* =============================================== Прослушка событий ================================================ */

// Событие - действие пользователя. Нажали на кнопку, перевели курсор, проскроллили и т.д.

/*
element.addEventListener('событие', функция(){})
*/

const btn = document.querySelector('#button');
const picture = document.querySelector('#logo');
btn.value = "Удалить";

//btn.addEventListener('click', function(){
//    console.log('Click!');
//    picture.remove(); // Удаляем элемент
//}) // название события, функция при запуске события

// Альтернативный способ обработать клик через element.onclick
btn.onclick = function(){
    console.log('Click!');
    img.remove();
}


/* =============================================== Работа с прослушкой события (2) ================================== */
const inputText = document.querySelector('#input-text');
const textBlock = document.querySelector('#text-block');

// Выводим в консоль значение пользователя
inputText.addEventListener('input', function(){
    console.log(inputText.value);
    textBlock.innerText = inputText.value; // Выводим введённый пользователем текст в инпуте под инпутом
})

// innerText - свойство DOM-элемента в JS, позволяющеее получить или установить текстовое содержимое элемента и его потомков


/* =============================================== Работа с прослушкой события (3) ================================== */

/*
event - объект, содержащий всё информацию о произошедшем событии
event.target - ссылается на html-элемент, на который было совершено событие <button>, <li> и т.д.
*/

const list = document.querySelector('#list');

list.addEventListener('click', function(event) {
    console.log(this);
    console.log(event);
    console.log(event.target);
})

/* =============================================== Создание элементов =============================================== */

/*
// Создать элемент
document.createElement('tag-name');

// Изменить содержимое HTML внутри документа
element.innerHTML = ''

// Изменить текстовое содержимое внутри элемента
node.innerText = ''

// Клонирование элемента
node.cloneNode() // true с внутренним содержимым (текст и теги), иначе - false

// Вставить элемент внутрь другого элемента
element.append(nodesOrDOMSStrings)

// Удалить элемент
element.remove()
*/

const container = document.querySelector('#elementsContainer');

// Создание заголовка
const newHeader = document.createElement('h1');
newHeader.innerText = 'Новый заголовок';
container.append(newHeader);

// Клонирование шапки
const mainHeader = document.querySelector('header');
const headerCopy = mainHeader.cloneNode(true) // true - копировать со внутренним содержимым
container.append(headerCopy);

// Вставка разметки через строки
const htmlExample = '<h2>Ещё один заголовок</h2>';
container.insertAdjacentHTML('beforeend', htmlExample);

// Вставка разметки через шаблонные строки
const title = 'Текст заголовка';
const htmlEx = `<h2>${title}</h2>`;
container.insertAdjacentHTML('beforeend', htmlEx);























