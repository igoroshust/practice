/* Пример вызова функции в параметрах другой функции */
function calculateSum(x, y) {
    let result = x + y;
    return result; // 15
}
let res = calculateSum(calculateSum(10, 20), calculateSum(30, 40));
console.log(res);



/* SWITCH CASE. Проверка значения переменной на различные варианты (альтернатива if-else)
    + улучшает читабельность кода при множестве условий 
    switch (выражение) {
        case значение:
            // Код для выполнения, если выражение == значение
            break;
        default:
            // Код, если ни один case не подошёл
            break;
    } 
*/

const mark = 5;

switch (mark){
    case 5:
        console.log('Awesome!');
        break; // Если break не закомментировать, следующий case отработает автоматически
    case 4:
        console.log('Good.');
        break;
    case 3:
        console.log('Neighter good, not bad.');
        break;
    case 2:
        console.log('Bad.');
        break;
    case 1:
        console.log('Terrible.');
        break;
    default:
        console.log('Value out of case.');
        break;
}


/* Пример функции с умножением числа на само себя */

// Метод repeat()
let b = 'b';
let output = b.repeat(3);
console.log(output); // bbb

// Функция (моя)
let a = 'a';

function mult(variable, count){
    let resultValue = variable;

    for (let i = 1; i < count; i++){
        resultValue += variable;
    }
    return resultValue;
}

let result = mult(a, 5);
console.log(result);

/* Пример добавления finally в for */
function example(){
    try {
        for (let i = 0; i < 10; i++) {
            console.log('i = ' + i);
            if (i == 5) break; // Или throw new Error();
        }
    } finally {
        console.log('Это выполнится всегда (finally)');
    }
}
example();


/* Создать новый файл через консоль powershell 
fsutil file createnew "doc.js" 0
0 - размер файла в байтах (пустой) */