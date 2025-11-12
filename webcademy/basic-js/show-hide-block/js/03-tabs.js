const header = document.querySelectorAll('.list-group-item');
const cards = document.querySelectorAll('.card');


// const headers = document.getElementsByTagName('h3');

header.forEach((item) => {

    item.addEventListener('click', () => {

        let findActiveCard;

        cards.forEach(card => { 
            if (card.classList.value == 'card p-3') {
                findActiveCard = card;
                card.classList.add('tab-content-hidden');
            }
        });

        const currentTab = item.getAttribute('data-tab');
        const goalElement = document.getElementById(currentTab);

        if (findActiveCard) {
            goalElement.classList.toggle('tab-content-hidden');
            findActiveCard.classList.add('tab-content-hidden');
        } else {
            goalElement.classList.toggle('tab-content-hidden');
        }
    });
});