const header = document.querySelectorAll('.list-group-item');
const tabList = document.querySelector('.list-group'); // ul
const cards = document.querySelectorAll('.card');


/* Решение учителя */
const tabHeaders = document.querySelectorAll('[data-tab]'); // Находим все заголовки табов по data-атрибуту
const contentBoxes = document.querySelectorAll('[data-tab-content]'); // Находим все контент-боксы

tabHeaders.forEach(function(item){
    item.addEventListener('click', function(){

        // 1. Скрыть все contentBox
        contentBoxes.forEach(function(item){
            item.classList.add('tab-content-hidden');
        });

        // 2. Выбираем нужный contentBox и показываем его
            // Получаем значение элемента, по которому кликнули
            // (!) Используем константу вместо let, потому что по клику код каждый раз запускается заново
        const contentBox = document.querySelector('#' + this.dataset.tab); // Находим нужный элемент на странице
        contentBox.classList.remove('tab-content-hidden'); // Показываем элемент
    })
})









/* Моё решение */
// header.forEach((item) => {
//     item.addEventListener('click', () => {

//         let findActiveCard;

//         cards.forEach(card => { 
//             // Скрываем активный элемент + запоминаем его
//             if (card.classList.value == 'card p-3') {
//                 findActiveCard = card; 
//                 card.classList.add('tab-content-hidden');
//             }
//         });

//         // Находим контент для кликнутого элемента
//         const goalElement = document.getElementById(item.getAttribute('data-tab'));

//         // Меняем видимость элемента на противоположную
//         goalElement.classList.toggle('tab-content-hidden');

//         // Скрываем другие активные табы
//         if (findActiveCard) {
//             findActiveCard.classList.add('tab-content-hidden');
//         }
//     });
// });


/* Решения ИИ */
/* Способ-1: Использование классов для состояния (без поиска активного) */
// header.forEach((item) => {
//     item.addEventListener('click', () => {
//         const goalElement = document.getElementById(item.getAttribute('data-tab'));

//         // Если таб уже активен - сворачиваем
//         if (item.classList.contains('active')) {
//             item.classList.remove('active');
//             goalElement.classList.add('tab-content-hidden');
//             return;
//         }

//         // Убираем активность со всех и добавляем к кликнутому
//         header.forEach(h => h.classList.remove('active'));
//         cards.forEach(c => c.classList.add('tab-content-hidden'));
//         item.classList.add('active');
//         goalElement.classList.remove('tab-content-hidden');
//     });
// });

/* Способ-2: Делегирование событий (один слушатель на родителе; меньше слушателей - лучше производительность) P.S. При клике нет сворачивания*/
// tabList.addEventListener('click', (event) => {
//     if (event.target.classList.contains('list-group-item')) {
//         const item = event.target;
//         const currentTab = item.getAttribute('data-tab');
//         const goalElement = document.getElementById(currentTab);

//         // Если клик на активный таб - сворачиваем его
//         if(!goalElement.classList.contains('tab-content-hidden')) {
//             goalElement.classList.add('tab-content-hidden');
//             return;
//         }

//         // Иначе: скрываем всё и показываем нужный
//         cards.forEach(card => card.classList.add('tab-content-hidden'));
//         goalElement.classList.remove('tab-content-hidden');
//     }
// })