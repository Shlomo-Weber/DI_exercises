var array = ["herp", "derp", "herpderp"]


// for (i in array ){
// 	console.log(i);
// }


// for of statement

// for (i of array){
// 	console.log(i);
// }


// forEach statement

// array.forEach( (x , i) =>{
// 	console.log(x, i);
// }
// );


// const detailedbasket = {
// 	apples: 5,
// 	oranges: 10,
// 	pears: 20
// }

// for (x in detailedbasket) {
// 	console.log(detailedbasket[x]);
// }

// Objects
// Object.keys(detailedbasket).forEach( key => {
// 	console.log(detailedbasket);
// }
// );

// let family = {
// 	john: 20,
// 	dale: 30,
// 	frederick: 48
// }

// for (i in family) {
// 	console.log(i);
// }

var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
};
// Display the number of levels in the building

// console.log(building.number_levels);

// Display how many apartments are on level 1 and 3. Do the sum of these apartments
// var aptlevel = Aptsperlvl(1) + Aptsperlvl(3)
// console.log("There are " + aptlevel + " apartments on 1 and 3");

// console.log(Aptsperlvl());
// function Aptsperlvl(level) {
// 	var apts = building.number_of_apt_by_level[level];
// 	return apts;
// }

// console.log(building.name_of_tenants[1],building.number_of_rooms_and_rent.Dan[0]);

// const arr = [5,0,9,1,7,4,2,6,3,8];
// let temp;
// for (var i = 0; i < arr.length; i++) {
// 	for (s = i; s<arr.length; s++) {
// 		if (arr[i] < arr[s]) {
// 			temp = arr[s];
// 			arr[s] = arr[i];
// 			arr[i] = temp;
// 		}	
// 	}
// }
// console.log(arr)

