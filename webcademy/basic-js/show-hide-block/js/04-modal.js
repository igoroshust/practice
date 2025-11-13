const modalButtons = document.querySelectorAll('[data-modal-button]');
const modalCloseButtons = document.querySelectorAll('[data-modal-close]');
const allModals = document.querySelectorAll('[data-modal]');

/* Кнопки - Открыть модалку */
modalButtons.forEach(function(item){
    item.addEventListener('click', function(){
        // Получаем ID модального окна
        const modalId = this.dataset.modalButton;

        // Находим модальное окно по ID
        const modal = document.getElementById(modalId);
        //const modal = document.querySelector("#" + modalId); // Вариант учителя

        // Выводим модалку на странице
        modal.classList.remove('content-hidden');

        /* Предотвращаем закрытие по клику на контент */
        // Находим внутри открываемой модалки блок .modal-window и запрещаем ему передавать клики "наверх" (по цепочке его родителей)
        modal.querySelector('.modal-window').addEventListener('click', function(event){
            event.stopPropagation(); // Отменяем передачу события наверх
        });
    });
});

/* Кнопки - Закрыть модалку */
modalCloseButtons.forEach(function(item){
    item.addEventListener('click', function(){
        // Находим родителя модалки
        const modal = this.closest('[data-modal]') // this - сама кнопка; closest - поиск среди родителей (по селектору)

        // Закрываем модалку
        modal.classList.add('content-hidden');
    });
});

/* Закрытие модалок при клике на бэкграунд */
allModals.forEach(function(item){
    item.addEventListener('click', function(){
        this.classList.add('content-hidden');
    });


    /* Блокируем скрытие модалки при клике на содержимое окна (текст, заголовки) -- предотвращаем поднятие элемента (родитель не участвует в поведении потомка) */
    // Код закомментирован, потому что логика вынесена в первый блок modalButtons(forEach)
    
    // Перехватываем событие на .modal-window
    // item.querySelector('.modal-window').addEventListener('click', function(event){
    //     event.stopPropagation();
    // });
});
