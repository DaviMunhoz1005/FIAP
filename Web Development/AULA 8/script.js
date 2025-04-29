function sum(x, y) {
    return x + y;
}

function sub(x, y) {
    return x - y;
}

function mult(x, y) {
    return x * y;
}

function div(x, y) {
    return x / y;
}

function calculator() {
    let firstNumber = Number(prompt("Enter a number: "));
    let secondNumber = Number(prompt("Enter another number: "));
    let userChoice = Number(prompt("Choose one option - 1: Sum, 2: Subtract, 3: Multiply, 4: Divide"));

    switch(userChoice) {
        case 1:
            console.log(`The sum of ${firstNumber} + ${secondNumber} = ${sum(firstNumber, secondNumber)}`);
            break;
        case 2:
            console.log(`The subtraction of ${firstNumber} - ${secondNumber} = ${sub(firstNumber, secondNumber)}`);
            break;
        case 3:
            console.log(`The multiplication of ${firstNumber} * ${secondNumber} = ${mult(firstNumber, secondNumber)}`);
            break;
        case 4:
            if (secondNumber === 0) {
                console.log("Cannot divide by zero!");
            } else {
                console.log(`The division of ${firstNumber} / ${secondNumber} = ${div(firstNumber, secondNumber)}`);
            }
            break;
        default:
            console.log("Please select a valid option.");
            calculator();
    }
}

calculator();