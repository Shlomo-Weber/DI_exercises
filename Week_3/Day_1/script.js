// let elem = document.getElementById("main");
// elem.setAttribute('width', '100');
// console.log(elem);

// let div1 = document.getElementById('page');
// let att = div1.getAttribute('ziv');
// console.log(att);
// div1.setAttribute('ziv','gggg');
// att = div1.getAttribute('ziv');
// console.log(att);

// let elem = document.getElementById('title')
// console.log(elem.innerText);

// let elem = document.getElementById('content');

// let myH1 = document.createElement('h1'); //This can create elements 
// myH1.innerText = "whatever I want";

// elem.appendChild(myH1); //Must use 'appendChild' to make the change

// let elem = document.getElementById('content');
// let elem1 = document.getElementById('title');

// let arr = ['ziv', 'jason', 'sara', 'rachel'];
//  for (i =0; i< arr.length; i++) {
//  	let user = document.createElement('h4');
//  	user.innerText = arr[i];
//  	user.innerText = "This is some random text";
//  	elem.appendChild(user);
//  	// elem1.appendChild(user);
// ; }

// let elem = document.getElementById('header');
// console.log(elem.firstElementChild);
// console.log(elem.lastElementChild);
// console.log(elem.nextElementSibling);

// let elem1 = document.getElementById('content');
// // console.log(elem1.previousElementSibling);

// // console.log(elem.parentNode);
// // console.log(elem.children);
// // for (1=0; i<elem.children.length; i++){
// // 	console.log(elem.children[i].innerText);
// // 	}
// // console.log(elem.nodeValue);
// // console.log(elem.nodeType);
// // console.log(elem.nodeName);


// let elem = document.getElementById('content');
// console.log(elem.innerText);

let elem = document.getElementById('content');
let txt = document.createTextNode('WEFBwefwEHADHFVJZSDB');
elem.appendChild(txt);
console.log(txt.nodeType);

console.log(elem.innerHTML);

console.log(elem.setAttribute('ziv', '100'));
console.log(elem.getAttribute('ziv'))

let elem1 = document.createElement('h1');
elem1.innerText = "Hello there. Generel Kenobi, you are a bold one";
elem.appendChild(elem1);

// console.log(elem.insertBefore(elem1,txt)); //inserts the first element before the second
// elem.removeChild(txt); // Removes a child element
let herp = document.getElementById('herp');
elem.replaceChild(elem1,herp); // Replaces one of the elements 