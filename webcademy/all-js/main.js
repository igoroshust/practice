// const myObject = {
//     city: '',
//     region: '',
//     country: ''
// }


const city = document.getElementById('city');
const region = document.getElementById('region');
const country = document.getElementById('country');

const modal = document.querySelector('.modal');
const modalParagraph = document.querySelector('.modal-paragraph');
const modalBtn = document.querySelector('.modal-btn');

const cityContent = 'City Content';
const regionContent = 'Region Content';
const countryContent = 'Country Content';

const citySection = document.querySelector('.city-section');
const cityBtn = document.querySelector('.city-btn');

cityBtn.addEventListener('click', function(e){
    e.stopPropagation();
    fetchData();
});


// citySection.addEventListener('click', function(e){
//     let currentElement = e.target;
//     let currentElementId = e.target.id;
    
//     if (currentElementId) console.log(currentElementId);

//     modal.classList.remove('hidden');

//     switch (currentElementId) {
//         case 'city':
//             modalParagraph.innerText = cityContent;
//             break;
//         case 'region':
//             modalParagraph.innerText = regionContent;
//             break;
//         case 'country':
//             modalParagraph.innerText = countryContent;
//             break;
//         default:
//             console.log('message')
//             break;
//     }
// });

// for (let i = 0; i < citySection.children.length; i++) {
//     console.log(citySection.children[i])
// }

for (const element of citySection.children) {
    element.addEventListener('click', function(e){
        let currentElement = e.target;
        let currentElementId = e.target.id;

        modal.classList.toggle('hidden');

        switch (currentElementId) {
            case 'city':
                modalParagraph.innerText = `${city.textContent.slice(city.textContent.lastIndexOf(':')+1).trim()} - ${cityContent}`;
                break;
            case 'region':
                modalParagraph.innerText = `${region.textContent.slice(region.textContent.lastIndexOf(':')+1).trim()} - ${regionContent}`;
                break;
            case 'country':
                modalParagraph.innerText = `${country.textContent.slice(country.textContent.lastIndexOf(':')+1).trim()} - ${countryContent}`;
                break;
            default:
                return;
        }
    })
}



async function fetchData() {
    try {
        const url = 'https://ipinfo.io/200.185.160.93/geo' // 200 - Sao Paulo, 161 - NY
        const response = await fetch(url);
        const data = await response.json();

        // Обновляем только динамические части
        document.querySelector('#city .value').textContent = data.city;
        document.querySelector('#region .value').textContent = data.region;
        document.querySelector('#country .value').textContent = data.country;

        // myObject.city = data['city']
        // myObject.region = data['region']
        // myObject.country = data['country']

        // if (city.textContent.slice(city.textContent.lastIndexOf(':')+1).trim() != data['city']){
        //     city.insertAdjacentHTML('beforeend', data['city']);
        // }
        // if (region.textContent.slice(region.textContent.lastIndexOf(':')+1).trim() != data['region']){
        //     region.insertAdjacentHTML('beforeend', data['region']);
        // }
        // if (country.textContent.slice(country.textContent.lastIndexOf(':')+1).trim() != data['country']){
        //     country.insertAdjacentHTML('beforeend', data['country']);
        // }

        // city.insertAdjacentHTML('beforeend', `${city.textContent.slice(0, city.textContent.lastIndexOf(':')+1).trim()} ${data['city']}`);
        // region.textContent = `${region.textContent.slice(0, region.textContent.lastIndexOf(':')+1).trim()} ${data['region']}`;
        // country.innerText = `${country.textContent.slice(0, country.textContent.lastIndexOf(':')+1).trim()} ${data['country']}`;

    } catch (error) {
        console.error(error);
    }
};

// fetchData();

// city.addEventListener('click', function(){
//     modal.classList.remove('hidden');
//     modalParagraph.innerText = cityContent;
// });

// region.addEventListener('click', function(){
//     modal.classList.remove('hidden');
//     modalParagraph.innerText = regionContent;
// });

// country.addEventListener('click', function(){
//     modal.classList.remove('hidden');
//     modalParagraph.innerText = countryContent;
// });




modalBtn.addEventListener('click', function(){
    modal.classList.add('hidden');
});
