console.log("Hello world")
// 🔹 Issues with var:

// It can be redeclared (which might cause bugs).
// It is hoisted (moves to the top of the scope).
// It has function scope, meaning it’s accessible within the entire function.

var name = "Rahul";  // Declare a variable
console.log(name);
document.write(name)    // Output: Rahul

var name = "Kumar";   // Re-declaring is allowed
console.log(name);    // Output: Kumar
document.write(name)    // Output: Rahul

let age = 25;
console.log(age); // Output: 25

age = 30;         // Allowed: Reassigning is possible
console.log(age); // Output: 30

// let age = 35;  ❌ Not allowed: Cannot redeclare a let variable in the same scope


const PI = 3.1416;
console.log(PI); // Output: 3.1416

// PI = 3.15; ❌ Error: Cannot reassign a constant variable

// const PI = 3.14; ❌ Error: Cannot redeclare a constant


// This is a single-line comment
let x = 10;  // Assigning value 10 to x
console.log(x);



/*
This is a 
multi-line comment
*/
let y = 20;
console.log(y);
