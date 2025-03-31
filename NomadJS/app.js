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
