// using for loop
function factorialize(num) {
    let total = 1
    for (let i = 1; i <= num; i++) {
        total *= i
    }
    return total
}

// using recursion
function factorialize(num) {
    if (num <= 1) return 1;
    else {
        return num * factorialize(num - 1)
    }
}
