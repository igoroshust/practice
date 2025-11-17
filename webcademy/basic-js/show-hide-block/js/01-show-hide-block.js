const button = document.querySelector('#button');
const content = document.querySelector('#content');


/* Решение учителя */
button.addEventListener('click', function(){
    console.log('Click!');
    
    if (content.classList.toggle('content-hidden')) {
        // content.classList.toggle выполнится в любом случае, а условие также выполняется, потому что toggle возвращает true или false
        button.textContent = "Открыть блок";
    } else {
        button.textContent = "Закрыть блок";
    }

    /* Пошаговое решение 
    content.classList.toggle('content-hidden');

    if (content.classList.contains('content-hidden')){
        button.innerText = "Открыть блок";
    } else {
        button.innerText = "Закрыть блок";
    }
    */
});


/* Моё решение */
// const openText = button.dataset.openText;
// const closeText = button.dataset.closeText;

// button.onclick = () => {
//     content.classList.toggle('content-hidden');
//     button.innerText = content.classList.contains('content-hidden') ? openText : closeText;
// };


/* Вариант решения от ИИ */
// function initShowHideBlock() {
//     const btn = document.querySelector('.show-hide-btn');
//     const paragraph = document.querySelector('.show-hide-paragraph');
    
//     const openText = btn.dataset.openText || 'Открыть блок';
//     const closeText = btn.dataset.closeText || 'Закрыть блок';
    
//     // Безопасность
//     if (!btn || !paragraph) {
//         console.warn('Элементы .show-hide.btn или .show-hide-paragraph не найдены.');
//         return;
//     }
    
//     btn.addEventListener('click', function(){
//         paragraph.classList.toggle('hidden');
//         btn.textContent = paragraph.classList.contains('hidden') ? btn.dataset.openText : btn.dataset.closeText;
//     });
// }    

// // Запуск после загрузки DOM
// document.addEventListener('DOMContentLoaded', initShowHideBlock);