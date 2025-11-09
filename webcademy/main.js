/* Несколько асинхронных операций (серия промисов) */
function checkRooms() {
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            console.log('---- checkRooms ----');
            console.log('Проверяем номера в отеле...');
            let availableRooms = true;

            if (availableRooms) {
                resolve('Номера есть!');
            } else {
                reject('Номеров нет.');
            }
        }, 1500);
    });
}

function checkTickets(data) {
    return new Promise(function(resolve, reject){
        setTimeout(() => {
            console.log('---- checkTickets ----');
            console.log('Ответ на предыдущем шаге:', `"${data}"`);

            console.log('Проверяем авиабилеты...');
            // ---- код отправки запроса в авиакомпанию ----
            const availableTickets = true;

            if (availableTickets) {
                let message = 'Билеты есть!';
                resolve(message);
            } else {
                let message = 'Билетов нет.';
                reject(message);
            }
        })
    })
}

function submitVacation(data) {
    console.log('---- submitVacation ----');
    console.log('Ответ на предыдущем шаге: ', `"${data}"`);
    console.log('Едем в отпуск!');
}

function cancelVacation(data) {
    console.log('---- cancelVacation ----');
    console.log('Ответ на предыдущем шаге: ', data);
    console.log('Отпуск отменяется.')
}

async function checkVacation(){
    // try-catch - важное условие обработки асинхронных функций, без него нельзя отловить reject и обрабатывать ошибки
    try {
        const roomsResult = await checkRooms();
        const ticketsResult = await checkTickets(roomsResult);

        if (ticketsResult) {
            submitVacation(ticketsResult);
        } else {
            cancelVacation(ticketsResult);
        }
    } catch (error) {
       cancelVacation(error);
    }
}

checkVacation();


/* Async functions. Асинхронные функции. Потребление промиса */
function promiseFunction() {
    return new Promise(function(resolve, reject){
        setTimeout(() => {
            result = false;
            if (result) {
                resolve('DONE!');
            } else {
                reject('FAIL!');
            }
        }, 1000);
    });
}

console.log(promiseFunction()); // Promise {<pending>}

// Потребление промиса с помощью асинхронной функции + try/catch (альтернатива then/catch) 
async function startPromise() {
    try {
        const result = await promiseFunction(); // Записываем результат выполнения promiseFunction()
        console.log(result);
    } catch(err) {
        console.log(err);
    }
};

startPromise();