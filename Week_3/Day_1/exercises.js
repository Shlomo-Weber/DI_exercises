// let div = document.getElementById('div');
// let list = document.getElementById('ul')
// console.log(div);


// Exercise 1

// //div Node
// console.log(document.body.firstElementChild);
// console.log(document.body.childNodes[1]);

// //ul Node 
// console.log(document.body.childNodes[3]);
// console.log(document.body.childNodes[2].nextSibling);

// //second li Node 
// console.log(document.body.childNodes[3].lastElementChild);
// console.log(document.body.childNodes[3].firstElementChild.nextElementSibling);

// Exercise 2
//1. 
// document.body.firstElementChild.style.backgroundColor ="lightblue";
// document.body.firstElementChild.style.padding ="20px";

// // //2. 
// document.body.childNodes[3].removeChild(document.body.childNodes[3].firstElementChild);
// document.body.childNodes[3].firstElementChild.style.border="red solid 3px";
// //3. 
// document.body.style.fontSize='3em';
// let background = document.body.firstElementChild.style.backgroundColor;
// if (background == "lightblue"){
// 	alert ("Hello there, General Kenobi");
// }

// Exercise 3
//1.
let elem = document.getElementById('container');
// console.log(elem);
//2.
//console.log(document.body.childNodes[3]);
let lists = document.getElementsByClassName('list');
// console.log(lists[0].childNodes[1]);
for (list of lists){
	console.log(list)
}
