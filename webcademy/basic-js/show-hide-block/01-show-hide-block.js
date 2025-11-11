const blockContent = document.querySelector('#content');
const btnContent = document.querySelector('#button');

const openText = btnContent.dataset.openText;
const closeText = btnContent.dataset.closeText;

btnContent.onclick = () => {
    blockContent.classList.toggle('content-hidden');
    btnContent.innerText = blockContent.classList.contains('content-hidden') ? openText : closeText;
};