// Write a JavaScript function that reverses a number.
// Sample Data and output:
// Example x = 32243;
// Expected Output: 34223

function reverse_number(n){
   n=n+ ""
    console.log(n)
    return n.split("").reverse().join("")
}

console.log(reverse_number(1234))


// Write a JavaScript function that returns a string that has letters in alphabetical order.
// Example string: 'webmaster'
// Expected Output: 'abeemrstw'

function alphabet_order(str){
    return str.split("").sort().join("")
}

console.log(alphabet_order("helloworld"))

// 5. Write a JavaScript function that accepts a string as a parameter and converts the first letter of each word into upper case.
// Example string : 'the quick brown fox'
// Expected Output : 'The Quick Brown Fox '


function uppercase(str){
    var array1=str.split(" ")
    var newarray= []
    for (var x=0;x<array1.length;x++){
        newarray.push(array1[x].charAt(0).toUpperCase()+array1[x].slice(1));
    }
    return newarray.join(" ")
}
console.log(uppercase("the quick brown fox"))