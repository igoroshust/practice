const header = document.querySelectorAll('.list-group-item');
const tabList = document.querySelector('.list-group'); // ul
const cards = document.querySelectorAll('.card');

/* Решения ИИ */

/* Способ-1: Использование классов для состояния (без поиска активного) */
header.forEach((item) => {
    item.addEventListener('click', () => {
        const goalElement = document.getElementById(item.getAttribute('data-tab'));

        // Если таб уже активен - сворачиваем
        if (item.classList.contains('active')) {
            item.classList.remove('active');
            goalElement.classList.add('tab-content-hidden');
            return;
        }

        // Убираем активность со всех и добавляем к кликнутому
        header.forEach(h => h.classList.remove('active'));
        cards.forEach(c => c.classList.add('tab-content-hidden'));
        item.classList.add('active');
        goalElement.classList.remove('tab-content-hidden');
    });
});



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
