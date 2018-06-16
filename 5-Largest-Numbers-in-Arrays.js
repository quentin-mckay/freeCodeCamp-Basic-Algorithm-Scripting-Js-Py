// accepts any number of subarrays
function largestOfFour(arr) {
    return arr.map(subarray => Math.max(...subarray))
}

let test = [[4, 5, 1, 3], 
            [13, 27, 18, 26], 
            [32, 35, 37, 39], 
            [1000, 1001, 857, 1]]
console.log(largestOfFour(test))
