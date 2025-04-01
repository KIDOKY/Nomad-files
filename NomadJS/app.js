/*
const a = 5;
const b = 2;
let myName = "kido";

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log("hello " + myName);

myName = "kidok";

console.log("your new name is " + myName);
*/

/*
const amIFat = null;
let something;
console.log(something, amIFat);
*/

/*
const daysOfWeek = ["Mon", "tue", "Wed", "thu", "fri", "sat"];

// Get Item from Array
console.log(daysOfWeek);

// Add one more day to the array
daysOfWeek.push("sun");

console.log(daysOfWeek);
*/

/*
const player = {
  name: "kido",
  points: 10,
  fat: true,
};

console.log(player);
player.fat = false;
player.lastName = "potato";
player.points = player.points + 15;
console.log(player);
*/

/*
function sayHello() {
  console.log("Hello my name is C");
}

sayHello("nico");
sayHello("dal");
sayHello("lynn");
*/

/*
function sayHello(nameOfPerson, age) {
  console.log("Hello my name is " + nameOfPerson + " and I'm " + age);
}

sayHello("nico", 10);
sayHello("dal", 23);
sayHello("lynn", 21);
*/

/*
function plus(firstNumber, secondNumber) {
  console.log(firstNumber + secondNumber);
}
function divide(a, b) {
  console.log(a / b);
}
plus(60, 8);
divide(98, 20);
*/

/*
const player = {
  name: "nico",
  sayHello: function (otherPersonsName) {
    console.log("hello " + otherPersonsName + " nice to meet you!");
  },
};

player.sayHello("lynn");
player.sayHello("nico");
*/

/*
const toBuy = ["potato", "tomato", "pizza"];

console.log(toBuy);
toBuy[2] = "water";
console.log(toBuy);
toBuy.push("meat");
console.log(toBuy);
*/

/*
const player = {
  name: "Nico",
  age: 98,
};
console.log(player);

player.name = "kido";
console.log(player);
player.sexy = "soon";
console.log(player, console);
*/

/*
function minusFive(potato) {
  console.log(potato - 5);
}

minusFive(10);
*/

/*
const calculator = {
  add: function (a, b) {
    console.log(a + b);
  },
  minus: function (a, b) {
    console.log(a - b);
  },
  div: function (a, b) {
    console.log(a / b);
  },
  multi: function (a, b) {
    console.log(a * b);
  },
  power: function (a, b) {
    console.log(a ** b);
  },
};

calculator.add(5, 1);
calculator.minus(3, 2);
calculator.div(4, 7);
calculator.multi(5, 2);
calculator.power(2, 8);
*/

/*
const age = 96;
function calculatorKrAge(ageOfForeigner) {
  ageOfForeigner + 2;
  return "hello";
}

const krAge = calculatorKrAge(age);

console.log(krAge);
*/

const calculator = {
  plus: function (a, b) {
    return a + b;
  },
  minus: function (a, b) {
    return a - b;
  },
  times: function (a, b) {
    return a * b;
  },
  divide: function (a, b) {
    return a / b;
  },
  power: function (a, b) {
    return a ** b;
  },
};

const plusResult = calculator.plus(2, 3);
const minusResult = calculator.minus(plusResult, 10);
const timesResult = calculator.times(10, minusResult);
const divideResult = calculator.divide(timesResult, plusResult);
const powerResult = calculator.power(divideResult, minusResult);
