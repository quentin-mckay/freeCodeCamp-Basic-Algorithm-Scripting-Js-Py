function frankenSplice(arr1, arr2, n) {
    let copy = arr2.slice()
    copy.splice(n, 0, ...arr1)
    return copy
}


console.log(frankenSplice([1, 2, 3], [4, 5], 1))