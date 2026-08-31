// forEach()

// Runs a function for each item in the array.

const fruits = ["kiwi", "mango", "apple", "pear"];

function printFruit(fruit) {
    console.log(fruit);
}

// fruits.forEach(printFruit);

// filter()
// Returns items that pass a condition.
number =[1,2,3,4,5,6]
function test(num){
    return num > 2;

}
// const result = number.filter(test);
// console.log(result)


// // map()
// // Creates a new array by changing each item.
// // const numbers = [1,2,3,4]

// function double(num){
//     return num * 2
// }
// const result = numbers.map(double)
// // console.log(result)


// Object {}
// Stores information using key-value pairs.
const person = {
    name : 'naima',
    age:25
}
console.log(person.name)


// 4. Set
// Stores unique values and removes duplicates.
const numbers = new Set([1, 2, 2, 3, 3]);

console.log(numbers);

// ⭐ Remember
// Array  → list of values
// Object → key + value
// Map    → key + value
// Set    → unique values