function findElement(arr, func) {
    return arr.find(func)
}


console.log(findElement([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; }))
console.log(findElement([1, 3, 5, 9], function(num) { return num % 2 === 0; }))