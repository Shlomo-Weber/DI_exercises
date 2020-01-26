// // Exercise 1
// var addNumber = [1];
// var addStreet = ["Hanarkis"];
// var country = ["Israel"];
// var global_add = addNumber.concat(addStreet,country);
// console.log(global_add)

// Exercise 2
// var pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];
// pets.push("horse");
// console.log(pets);
// pets.splice(3,1);
// console.log(pets);
// pets.length;

// Exercise 3
// var newDog = "poodle"
// // console.log(newDog.toLowerCase());
// console.log(newDog == "poodle");

// if (newDog == "cats") {
// 	alert("I LOVE poodles, theyre the best")
// }
// else {
// 		alert("i like cats instead")
// };

// Exercise 4
// var birthyr = 1995;
// var futureyr = 2035;
// var age = futureyr - birthyr;
// console.log("I will be " + age + " in " + futureyr);

// // Class Exercise
// let object1 = {
// 	username: "herp",
// 	password: "derp"
// }; 
// let object2 = {
// 	username: "herp",
// 	password: "derp"
// };
// let object3 = {
// 	username: "herp",
// 	password: "derp"
// };

// let database = [object1];

// let newsfeed = [object1, object2, object3];
// console.log(newsfeed);


// Gold Exercise 1 

// var number = prompt("Choose a number");

// checkEven();

// function checkEven() {
// 	if (number % 2 == 0) {
// 		alert( + " is an even number");
// 	}
// 	else {
// 		alert(number + " is not an even number");
// 	}
// }

// Gold Exercise 2
// var x = 5;
// var y = 10;

// if (x > y) {
// 	alert("Not bigger");}

// 	else {
// 		alert("bigger");
// 	}


// Gold Exercise 3

// var question = prompt("Which language do you speak");

// displayLanguage(question)

// function displayLanguage(lang) {
// 	if (lang == "French"){
// 		alert("Bonjour");
// 	}
// 	else if (lang == "English"){
// 		alert("Hello");
// 	}
// 	else if (lang == "Hebrew"){
// 		alert("Shalom");
// 	}
// 	else {
// 		alert(":D");
// 	}
// }

// Gold Exercise 4

// var grade = prompt ("What grade did you get?")

// getGrade(grade)

// function getGrade(grade) {
// 	if (grade >= 90) {
// 		alert("A");
// 	}
// 	else if (grade > 80) {
// 		alert("B");
// 	}
// 	 else if (grade > 70) {
// 	 	alert("C");
// 	 }
// 	else {
// 	 	alert("D"); 
// 	 }
// }

// switch(grade >= new Number()) {
// 	case grade >= 90:
// 	alert("A")
// 	break;
// 	case grade >= 80:
// 	alert("B")
// 	break;
// 	case grade >= 70:
// 	alert("C")
// 	break;
// 	case grade >= 60:
// 	alert("D")
// 	break;
// 	default: alert ("F");
// }

// Ninja Exercise 1

var me = ["my", "favorite", "color", "is", "blue"]
me.join(me);