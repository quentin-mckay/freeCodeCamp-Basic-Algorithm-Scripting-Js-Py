// using .substr()
// .substr(startIndex, length)
// -- if no length, go till end of string
// -- if startIndex is negative it goes from end of string
function confirmEnding(str, target) {
    return str.substr(-target.length) === target
}

// using regular expression
// $ character matches end of string
// string.match(rexexp) returns array of matches or undefined
// regexp.test(string) returns true or false
function confirmEnding(str, target) {
    const re = new RegExp(`${target}$`)  
    return re.test(str)  // 
}


// === tests ===
console.log(confirmEnding("Bastian", "n"))
console.log(confirmEnding("Congratulation", "on"))
console.log(confirmEnding("Open sesame", "pen"))