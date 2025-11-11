const button = document.querySelector('#button');
const content = document.querySelector('#content');

const openText = button.dataset.openText;
const closeText = button.dataset.closeText;

button.onclick = () => {
    content.classList.toggle('content-hidden');
    button.innerText = content.classList.contains('content-hidden') ? openText : closeText;
};