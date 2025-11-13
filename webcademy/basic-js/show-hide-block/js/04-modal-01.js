/* Реализация модалки для одного элемента (неуниверсальное решение, в образовательных целях) */


/* Решение учителя */
// Находим нужные элементы: кнопка модалки, модалка, кнопка закрытия
const button = document.querySelector('[data-modal-button]');
const modal = document.querySelector('[data-modal]');
const buttonClose = document.querySelector('[data-modal-close]');

// Прослушиваем клик на кнопке открытия и открываем модалку
button.addEventListener('click', function(){
    modal.classList.remove('content-hidden');
});

// Прослушиваем клик на кнопке закрытия и закрываем модалку
buttonClose.addEventListener('click', function(){
    modal.classList.add('content-hidden');
});

modal.addEventListener('click', function(){
    modal.classList.add('content-hidden');
    // console.log('Close modal');
});

// Предотвращаем всплытие элементов (чтобы избежать скрытия модалки при клике на текст внутри неё и другие дочерние элементы)
modal.querySelector('.modal-window').addEventListener('click', function(event){
    // console.log(event);
    event.stopPropagation(); // Останавливаем передачу события наверх (родители не узнают о произошедшем событии)
});



/* Вариант от ИИ */
// const buttons = document.querySelectorAll('[data-modal-button]');
// buttons.forEach(function(button){
//     const currentModal = document.getElementById(button.getAttribute('data-modal-button'));
//     const exitModal = currentModal.querySelector('[data-modal-close]'); 

//     // Устанавливаем обработчик закрытия один раз
//     exitModal.addEventListener('click', function(){
//         currentModal.classList.add('content-hidden');
//     });

//     // Обработчик открытия
//     button.addEventListener('click', function(event){
//         currentModal.classList.remove('content-hidden');
//     });
// });


/* Мой вариант */
// const buttons = document.querySelectorAll('[data-modal-button]');
// buttons.forEach(function(button){
//     button.addEventListener('click', function(event){
//         const currentModal = document.getElementById(button.getAttribute('data-modal-button'));
//         const exitModal = currentModal.querySelector('[data-modal-close]');
        
//         currentModal.classList.remove('content-hidden');

//         exitModal.addEventListener('click', function(){
//             currentModal.classList.add('content-hidden');
//         });
//     })
// });