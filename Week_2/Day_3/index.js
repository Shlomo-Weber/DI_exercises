// for (var i = 0 /*Start conditon*/; i < 10 /*End condition*/ ; i++ /*increment by one at a time*/ ) {
// 	console.log (i)
// }

// let arr = [1, 4, 7, 9];

// for (var i = 0; i < arr.length; i++) {
// 	console.log(arr[i]);
// } //If you want to find out how many/what elements are in an array, you dont have to count, this syntax will tell you. 

// let arr = ["Banana", "Apples", "Oranges", "Kiwi", "Blueberries"];

// for (let i = arr.length-1; i >= 0; i--){
// 	console.log(i, arr[i]);
// }

// Exercise 1
// for (var i = 0; i <= 15; i++) {
// 	if (i % 2==0){
// 		console.log(i + " This is even")
// 	}
// 	else {
// 		console.log (i + " this is odd");
// 	}
// }

// Exercise 2 

// for (i = 1; i <= 100; i++) {
// 	if (i % 3==0 && i % 5==0) {
// 		console.log ("fizzbuzz");
// 		}
// 	else if (i % 3==0) {
// 		console.log("fizz");
// 		}
// 	else if (i % 5==0){
// 		console.log("buzz");
// 		}
// 	else {
// 		console.log(i);
// 	}
	
// }

// Exercise 3

// var students = [
//   ['David', 80],
//   ['Vinoth', 77],
//   ['Divya', 88],
//   ['Ishitha', 95],
//   ['Thomas', 68]
// ];

// let average = 0;
// for (var i = 0; i < students.length; i++) {
// 	average = average + students[i][1];
// }
// // console.log(average/students.length);	



// for (var i = 0; i < students.length; i++) {
// 	let grade = students[i][1];
// 	let student = students[i][0]
// 	if ( grade < 60) {
// 		console.log(student + " received an F");
// 	}
// 	else if (grade < 70) {
// 		console.log(student + " received a D");
// 	}
// 	else if (grade <80) {
// 		console.log(student + " received a C");
// 	}
// 	else if (grade <90) {
// 		console.log(student + " received a B");
// 	}
// 	else {
// 		console.log(student + " received an A");
// 	}
// }

// Exercise 4
// let star = "*";
// let temp = "";
// for (var i = 1; i <= 5; i++) {
// 	temp = temp + star
// 	console.log(temp);
// }

// // Exercise 5 
// let colors = ["green", "black", "orange"];

// for (var i = 0; i >= 3; i++) {
// 	console.log(colors.[0]);
// }

var healthbar = 1;
var link;
var potion;
for (healthbar; healthbar <= 7; healthbar++) {
	console.log();
}