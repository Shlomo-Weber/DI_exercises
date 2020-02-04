
function playTheGame (){
	var CompNum=Math.floor(Math.random() * 10)
	var play=confirm("play the game?");
	var youlost = true;
	for(let i = 0; i <=2; i++){
		if (play==true) {
			var number=prompt("please choose a number between 1-10");
			if (number=="") {
				alert("thats not a number dumbass");
			}
			else if (number <0 || number > 10) {
				alert("Nice try jokester");
			}
			else if (isNaN(number)){
				alert("Thats not a number");
			}
			else {
				console.log(CompNum);
				let result = test(Number(number), CompNum);
				if (result == 1) {
					youlost = false;
					alert("You Won");
					break;
				}
				else if (result == 2) {
					alert("The computer number is bigger, guess again");
				}
				else if (result == 3) {
					alert("The computer number is smaller, guess again");
				}
			}
		}
		else {
			alert("okay then");
		}
	}
	if (youlost){
		alert("you can't guess again " + "the computer's number was " + CompNum);
	}

}
function test (myNumber, computerNumber){
		if (myNumber == computerNumber) {
			return 1;
		}
		else if (myNumber < computerNumber){
			return 2
		} 
		else if(myNumber > computerNumber){
			return 3;
		}
	}