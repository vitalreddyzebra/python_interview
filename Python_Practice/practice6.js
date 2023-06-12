let day="tuesday "
console.log(day)

// to find the lenght of string 

console.log(day.length)

// check whether 

let nameed = "Vital Reddy"

let after_split =nameed.split(" ")
console.log(after_split)

//Write a JavaScript function that hides email addresses to prevent unauthorized access.

//Test Data:
//console.log(protect_email("robin_singh@example.com"));
//"robin...@example.com"

function protect_email(user_email){
    var avg, splitted,part1,part2;
    splitted=user_email.split("@");
    part1=splitted[0];
    console.log(part1.length)
    avg=part1.length / 2;
    part1=part1.substring(0,(part1.length-avg));
    part2=splitted[1];
    return part1 + "...@" + part2;


}

console.log(protect_email("robin_singh@example.com"));



// Write a JavaScript function to parameterize a string.

// Test Data:
// console.log(string_parameterize("Robin Singh from USA."));
// "robin-singh-from-usa"


string_parameterize =function(str1){

    return str1.trim().toLowerCase().replace(/[^a-zA-Z0-9 -]/,"").replace(/\s/g,"-");
}

console.log(string_parameterize("Robin Singh from USA."));