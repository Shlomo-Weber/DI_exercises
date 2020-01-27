function c(text){
	console.log(text);
}

alert("Please select items to add to your cart");
let root = document.getElementById("root");
let div = document.createElement('div');
let untitledlist = document.createElement('ul');

div.appendChild(untitledlist);
root.appendChild(div);
// alert("What do you need to buy?");
function AddItem() {
	let item_to_add = prompt("Please add an item");{
	let listitem = document.createElement('li');
	div.appendChild(listitem);
	let shopping_item = document.createTextNode(item_to_add);
	listitem.appendChild(shopping_item);

	}
}

function RemoveItems(){
	div.remove();
	return;

}