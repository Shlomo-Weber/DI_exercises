const root = document.getElementById("root");
let bigbox = document.createElement('div');
let smallbox = document.createElement('div');
// big box
bigbox.style.width = '400px';
bigbox.style.height = '400px';
bigbox.style.position = 'relative';
bigbox.style.background = 'black';
// small box
smallbox.style.width = '50px';
smallbox.style.height = '50px';
smallbox.style.position = "absolute";
smallbox.style.background = "green";

root.appendChild(bigbox);
bigbox.appendChild(smallbox);

let strtbutton = document.getElementById('start');
let resetbutton = document.getElementById('reset');

// move box function
function movingBox(){
		let pos = 0;
		let id = setInterval(function (){
		if (pos == 350) {
			clearInterval(id);
		}
		else {
			pos++;
			smallbox.style.left = pos + 'px';
			smallbox.style.top = pos + 'px';
		}
	},5);
}

// Click me button
strtbutton.addEventListener('click', movingBox);

function resetBox(){
		let pos = 350;
		let id = setInterval(function (){
		if (pos == 0) {
			clearInterval(id);
		}
		else {
			pos--;
			smallbox.style.left = pos + 'px';
			smallbox.style.top = pos + 'px';
		}
	},5);
}
// Reset Button
resetbutton.addEventListener('click', resetBox);