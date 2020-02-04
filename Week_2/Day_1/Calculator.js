let button_1 = 0;
let button_2 = 0;
let symbol;

function my_f(button) {
	if (button == "+" || button == "-" || button == "/"|| button == "*") {
		symbol = button;
	}
	else if (button == "="){
		if (symbol == "+") {
			alert(button_1 + button_2);
	}
	 else if (symbol == "-") {
			alert(button_1 - button_2);
	}
	else if (symbol == "/") {
			alert(button_1 / button_2);
	}
	else if (symbol == "*") {
			alert(button_1 * button_2);
	}
else {
		if (button_1 == 0) {
		button_1 = button;
} 
		else {
		button_2 = button; 
	}
}