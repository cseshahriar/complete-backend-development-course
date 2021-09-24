// print out

/*
Multi 
line
comment
*/

console.log('Bismillah')

// variables
var x = 5;
var y = 6;
var sum = x + y;
console.log(`The summation of ${x} and ${y}: `, sum)

let n = 10
let m = 3
console.log(n/m)
console.log(n % m )

const PI = 3.1415926535
console.log(PI)


// operations
x = 5 
y = 6
console.log(x-y)
console.log(2**3)

++x 
console.log(x) // 6
x++
console.log(x)
x--
console.log(x)

console.log(typeof(x))

let name = 'Shahriar'
console.log(typeof(name))


// functions
console.log(eval('2 + 2'));
console.log('2'+'2') // 22


// user defined functions
function myFum(input1, input2) {  // Parameters
    let x = input1
    let y = input2
    return x + y
}

result = myFum(5, 8); // 5, 8 args
console.log(result); 


// array
let friends = ['Nazmul', 'Piyash', 25]
              // 0            1     2 
console.log(friends[0])
console.log(friends[2])

let friends_arr = [
    ['Nazmul', 25], // row, col
    //00      01
    ['Piyash', 28],
    //10       11
    ['Sakib', 24],
    // 20   21
]
console.log(friends_arr[1][0])
console.log(friends_arr[2][0])
console.log(friends_arr.length) 

// loop
let country = "Bangladesh";
let numbers = [1, 2, 5]

//          0      end                 increment
for(let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}



for (let i of numbers) {
    console.log(i)
}

for (const x of country) {
    console.log(x)
} 

for(key in numbers) {
    console.log(numbers[key]);
}

// while loop

let i = 2; // start
while(i >= 0) { // end
    console.log('----------', numbers[i])
    //i++; // increment
    i--;
} 


// conditional statements
var x = 5
var y = 6

if(x == y) {
    // block start
    console.log('True');

    //end

} else if(x < y) {
    console.log('x is less than y');
}
 else {
    console.log('False');
}