// using for loop
function repeatString(str, num) {
    let total = ''
    for (let i = 0; i < num; i++) {
        total += str
    }
    return total
}


// using .repeat()  (not allowed in exercise)
function repeatString(str, num) {
    return str.repeat(3)
}
