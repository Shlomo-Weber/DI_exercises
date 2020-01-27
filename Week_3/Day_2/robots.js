let root = document.getElementById("root")
c(root);

function c(text){
	console.log(text);
}

function myButton() {
	for (robot of robots){
		console.log(robot);
		let div = document.createElement('div');
		let img = document.createElement('img');
		let name = document.createElement('h2');
		let username = document.createElement('p');
		let email = document.createElement('p');

		img.setAttribute("src","https://robohash.org/" + robot.id + "?size=200x200");
		name.innerText = robot.name;
		username.innerText = robot.username;
		email.innerText = robot.email;


		div.appendChild(img);
		div.appendChild(name);
		div.appendChild(username);
		div.appendChild(email);

		div.classList.add('box');
		div.classList.add('singleborder');
		div.classList.add('solidborder');


		root.appendChild(div);

		
	}
}
function changeBorder() {
	let boxes = document.getElementsByClassName('box');
	for (box of boxes) {
		box.classList.toggle('solidborder');
	}
}
