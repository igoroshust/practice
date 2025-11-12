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