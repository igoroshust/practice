/* Прослушка событий */

const button = document.querySelector('#button');
const button1 = document.querySelector('#button1');
const picture = document.querySelector('#picture');

button.value = 'Удалить';

// Устанавливаем прослушку события (удаление по клику)
// addEventListener позволяет навешивать много обработчиков на 1 событие
button.addEventListener('click', function(){
    console.log('Click!');
    picture.remove(); // Удаляем картинку
});

// { capture: true } - действия на этапе захвата (будет выведено перед кликом)
button.addEventListener('click', function(){
    console.log('Захват!');
}, { capture: true });

// { once: true } - обработчик выполняется только один раз, затем автоматически удаляется. 
// Полезно для одноразовых действий с целью избежать утечек в памяти.
button1.addEventListener('click', function(){
    console.log('1 раз выполнюсь');
}, { once: true });

// { passive: true } - обработчик не будет вызывать `preventDefault()` (запрет стандартного поведения, например, прокрутки)
window.addEventListener('scroll', () => console.log('Скролл'), { passive: true })

button1.addEventListener('click', (e) => {
    e.preventDefault(); // Работает только при passive: false
    console.log('Клик без действия по умолчанию');
}, { passive: false });


// { signal: undefined } - позволяет отменить слушатель с помощью AbortController. Полезно для очистки при размонитровании компонентов (например, в React)
// signal отменяет только те обработчики, которые явно связаны с ним.
const controller = new AbortController();

button.addEventListener('click', () => console.log('Клик из signal'), { signal: controller.signal })

// Отмена всех связанных слушателей (через 2 секунды сигнал отменится)
setTimeout(() => {
    controller.abort();
    console.log('Сигнал отменён!');
}, 2000)


// Альтернативный способ навешивать события по клику
// Только 1 обработчик (дубли перезаписывают исходный)
button.onclick = function () {
    picture.remove(); // Удаляем картинку
}