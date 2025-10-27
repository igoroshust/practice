/* Пример итерации по объекту (Symbol не участвует) */
const id = Symbol();

let my_object = {
    [id]: 12,
    'name': 'Igor'
}

for (let key in my_object) {
    console.log(`Ключ: ${key}, Значение: ${my_object[key]}`);
}

/* Условный оператор */
const time = 20;

if (time < 12) {
    console.log('Доброе утро!');
} else if (time >= 12 && time < 18) {
    console.log('Добрый день');
} else {
    console.log('Добрый вечер');
}

/*Тернарный оператор */
// (условие) ? (условие верно) : (условие не верно);