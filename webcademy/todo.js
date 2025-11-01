/* Секундомер */
const counterElement = document.querySelector('#counter');
let counter = 0;
let timerID; // При  кажом запуске (старт) timerID будет меняться


// Старт
const buttonStart = document.querySelector('#start');
buttonStart.onclick = function(){
    console.log('Нажали на start')
    timerID = setInterval(function(){ // let, потому что несколько раз запускаем и останавливаем данные сетинтервал
        counter++;
        counterElement.innerText = counter;
    }, 1000);
};

// Пауза
const buttonPause = document.querySelector('#pause');
buttonPause.onclick = function(){
    console.log('Нажали на паузу')
    clearInterval(timerID);
};


// Сброс
const buttonReset = document.querySelector('#reset');
buttonReset.onclick = function(){
    console.log('Нажали на сброс');
    counter = 0;
    counterElement.innerText = counter;
    clearInterval(timerID);
};



/* Создание списка задач

const todoInput = document.querySelector('#todo-input');
const todoForm = document.querySelector('#todo-form');
const todoList = document.querySelector('#list');

todoForm.addEventListener('submit', formHandler);


function formHandler(event) {
    event.preventDefault(); // Отменяем стандартное поведение (перезагрузка страницы при отправке формы)

    // Получаем название задачи из инпута
    const taskText = todoInput.value;

    // Создаём тег li через разметку
    // const li = `<li>${taskText}</li>`;

    // Добавляем разметку на страницу
    // todoList.insertAdjacentHTML('beforeend', li);

    // Создаём тег li с помощью создания элемента
    const newTask = document.createElement('li');
    newTask.innerText = taskText;

    // Создаём кнопку удалить
    const deleteBtn = document.createElement('button');
    deleteBtn.setAttribute('role', 'button'); // Добавляем это кнопкам, не отправляющим формы, а выполняющим действия (удалить)
    deleteBtn.innerText = 'Удалить';
    deleteBtn.style['margin-left'] = '15px';
    newTask.append(deleteBtn);

    // Добавляем событие по клику (через обычную функцию)
    // deleteBtn.addEventListener('click', function(){
    //     this.closest('li').remove()
    // })

    // Добавляем событие через стрелочную функцию (e для работы с e.target (чтобы был this))
    deleteBtn.addEventListener('click', (e) => e.target.closest('li').remove());

    // // Удаляем элемент по клику
    // deleteBtn.onclick = () => newTask.remove();

    // Добавляем элемент на страницу
    todoList.append(newTask);

    // Очищаем поле ввода
    todoInput.value = '';

    // Фокус на поле ввода
    todoInput.focus();
}


// const todoButton = document.querySelector('#todo-button');

// todoButton.addEventListener('click', function(){
//     let newItem = document.createElement('li');
//     newItem.innerHTML = todoInput.value;
//     todoList.append(newItem);
// });

 */