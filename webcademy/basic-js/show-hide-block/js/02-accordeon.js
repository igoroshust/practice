// const headers = document.querySelectorAll("[data-name='accordeon-title']");

// /* Итоговый вариант */
headers.forEach((item) => {
    item.addEventListener('click', function(){
        // this содержит информацию о элементе, на который мы кликнули (ссылкается на заголовок, по которому пришёлся клик)
        // console.log(this);
        // console.log(this.nextElementSibling);
        this.nextElementSibling.classList.toggle('content-hidden');
    });
});

/* Вариант с отдельной функцией */
headers.forEach(function(item) {
    item.addEventListener('click', showContent); // showContent без вызова, т.к. внутри addEventListener передаёт ссылку на функцию как callback - она будет вызвана браузером при клике по умолчанию.
});

function showContent() {
    this.nextElementSibling.classList.toggle('content-hidden');
};


/* Моё решение */
// const accordeonTitle = document.querySelectorAll('.list-group-item.list-header');

// accordeonTitle.forEach((item, index) => {
//     accordeonTitle[index].onclick = () => {
//         accordeonTitle[index].nextElementSibling.classList.toggle('content-hidden');
//     }
// });