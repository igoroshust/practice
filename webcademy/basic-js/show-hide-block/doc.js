const blockContent = document.querySelector('#content');
const btnOpen = document.querySelector('#button');

const openText = btnOpen.dataset.openText;
const closeText = btnOpen.dataset.closeText;

// const openText = btnOpen.getAttribute('data-open-text');
// const closedText = btnOpen.getAttribute('data-closed-text');

btnOpen.addEventListener('click', () => {
    blockContent.classList.toggle('content-hidden');
    btnOpen.innerText = blockContent.classList.contains('content-hidden') ? openText : closeText;
});


