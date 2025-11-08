const city = document.querySelector('.city');


const apiInfo = fetch('https://ipinfo.io/161.185.160.93/geo')
.then(response => response.json())
.then(data => {
    text = document.createTextNode(data['city']);
    city.appendChild(text);
})
.catch(error => {
    console.error(error);
})

