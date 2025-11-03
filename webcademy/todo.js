/* Промисы. Нужны для решения проблемы асинхронного кода в JS так. С их помощью можно описать функции чётки и последовательно,
друг за другом + это выглядит аккуратее коллбеков и позволяет избежать callback hell

Промисы созданы для того, чтобы обернуть собой асинхронный код, выполнение которого необходимо подождать, и после него выполнять следующие действия 
в .then() мы передаём cb-функцию из категории 'resolve'. then при своей работе возвращает промис, то есть мы можем дальше работать с цепочкой.
тонкий момент, что then могут выполняться не строго по цепочке (например, если во втором then прописать setTimeout)

в .catch() мы передаём cb-функцию из категории 'reject' 

Плюсы промисов: 
1. Легко потребляется;
2. Удобно передавать функции без callback hell'a */

// Создаём промис
const myPromise = new Promise(function(resolve, reject){
    // resolve и reject - cb-функции, выполняемые при успешном или неуспешном выполнении промиса
    setTimeout(function(){
        // запрос на сервер
        const response = true; // от значения зависит обработка кода в then или catch
        if (response) {
            let message = 'SUCCESS';
            resolve(message); // Отработает then
        } else {
            let message = 'FAILED';
            reject(message); // Отработает catch
        }
    }, 1000);
    console.log('Promise created');
});

myPromise
.then(function(data){
    console.log('Then 1');
    console.log(data);
    return 'Data from then 1';
})
.then(function(data){
    console.log('Then 2');
    console.log(data); // Вывод 'Data from then 1', то есть второй then обработал результат выполнения первого then
})
.catch(function(data){
    console.log('Catch');
    console.log(data);
});


/* Пример промиса со сторой последовательностью выполнения цепочки (несмотря на разный setTimeout) */
const myPromise1 = new Promise(function(resolve, reject){
    // Имитируем ответ от сервера
    const response = true;
    if (response) {
        let message = "SUCCESS";
        resolve(message);
    } else {
        let message = "FAILED";
        reject(message);
    }
});

myPromise1
.then(function(data){
    return new Promise(function(resolve, reject){
        setTimeout(() => {
            console.log('Then 1');
            console.log(data);
            // Имитация ответа от сервера
            const response = true;
            if (response) {
                resolve('Data from then 1');
            } else {
                reject('Data from then 1');
            }
        }, 1000);
    });
})
.then(function(data){
    setTimeout(() => {
        console.log('Then 2');
        console.log(data); // Вывод Data from then 1
    }, 500);
})
.catch(error => console.error(error));




















// /* Секундомер */
// const counterElement = document.querySelector('#counter');
// let counter = 0;
// let timerID; // При  кажом запуске (старт) timerID будет меняться


// // Старт
// const buttonStart = document.querySelector('#start');
// buttonStart.onclick = function(){
//     console.log('Нажали на start')
//     timerID = setInterval(function(){ // let, потому что несколько раз запускаем и останавливаем данные сетинтервал
//         counter++;
//         counterElement.innerText = counter;
//     }, 1000);
// };

// // Пауза
// const buttonPause = document.querySelector('#pause');
// buttonPause.onclick = function(){
//     console.log('Нажали на паузу')
//     clearInterval(timerID);
// };


// // Сброс
// const buttonReset = document.querySelector('#reset');
// buttonReset.onclick = function(){
//     console.log('Нажали на сброс');
//     counter = 0;
//     counterElement.innerText = counter;
//     clearInterval(timerID);
// };



// /* Создание списка задач

// const todoInput = document.querySelector('#todo-input');
// const todoForm = document.querySelector('#todo-form');
// const todoList = document.querySelector('#list');

// todoForm.addEventListener('submit', formHandler);


// function formHandler(event) {
//     event.preventDefault(); // Отменяем стандартное поведение (перезагрузка страницы при отправке формы)

//     // Получаем название задачи из инпута
//     const taskText = todoInput.value;

//     // Создаём тег li через разметку
//     // const li = `<li>${taskText}</li>`;

//     // Добавляем разметку на страницу
//     // todoList.insertAdjacentHTML('beforeend', li);

//     // Создаём тег li с помощью создания элемента
//     const newTask = document.createElement('li');
//     newTask.innerText = taskText;

//     // Создаём кнопку удалить
//     const deleteBtn = document.createElement('button');
//     deleteBtn.setAttribute('role', 'button'); // Добавляем это кнопкам, не отправляющим формы, а выполняющим действия (удалить)
//     deleteBtn.innerText = 'Удалить';
//     deleteBtn.style['margin-left'] = '15px';
//     newTask.append(deleteBtn);

//     // Добавляем событие по клику (через обычную функцию)
//     // deleteBtn.addEventListener('click', function(){
//     //     this.closest('li').remove()
//     // })

//     // Добавляем событие через стрелочную функцию (e для работы с e.target (чтобы был this))
//     deleteBtn.addEventListener('click', (e) => e.target.closest('li').remove());

//     // // Удаляем элемент по клику
//     // deleteBtn.onclick = () => newTask.remove();

//     // Добавляем элемент на страницу
//     todoList.append(newTask);

//     // Очищаем поле ввода
//     todoInput.value = '';

//     // Фокус на поле ввода
//     todoInput.focus();
// }


// // const todoButton = document.querySelector('#todo-button');

// // todoButton.addEventListener('click', function(){
// //     let newItem = document.createElement('li');
// //     newItem.innerHTML = todoInput.value;
// //     todoList.append(newItem);
// // });

//  */