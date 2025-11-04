/* Работа с получением данных (API, async) */

// myObject = {
//     city: '',
//     region: '',
//     country: '',
// }

// fetch('https://ipinfo.io/161.185.160.93/geo')
// .then(response => response.json())
// .then(data => {
//     myObject.city = data['city'];
//     myObject.region = data['region'];
//     myObject.country = data['country'];
// })
// .catch(error => console.error('Ошибка', error))
// .finally(console.log('Операция завершена.'));


// setTimeout(() => {
//     console.log(myObject);

//     let headingCity = document.querySelector('.heading-city');
//     let regionCity = document.querySelector('.region-city');
//     let countryCity = document.querySelector('.country-city');

//     headingCity.innerText = myObject['city'];
//     regionCity.innerText = myObject['region'];
//     countryCity.innerText = myObject['country'];
// }, 2000);



let myObject = {
    city: '',
    region: '',
    country: '',
};

// Оборачиваем в асинхронную функцию (чтобы использовать await)
async function fetchData() {
    try {
        const response = await fetch('https://ipinfo.io/161.185.160.93/geo');
        const data = await response.json();
        
        // Заполняем объект данными
        myObject.city = data.city;
        myObject.region = data.region;
        myObject.country = data.country;
        
        console.log(myObject);  // Выводим объект сразу после получения данных
        
        // Обновляем DOM
        const headingCity = document.querySelector('.heading-city');
        const regionCity = document.querySelector('.region-city');
        const countryCity = document.querySelector('.country-city');
        
        headingCity.innerText = myObject.city;
        regionCity.innerText = myObject.region;
        countryCity.innerText = myObject.country;
        
    } catch (error) {
        console.error('Ошибка:', error);
    } finally {
        console.log('Операция завершена.');
    }
}

// Вызываем функцию
fetchData();
