function getIndexToIns(arr, num) {
    arr.sort((a, b) => a - b) // sort occurs IN PLACE !
    const result = arr.findIndex(val => num <= val)
    return result === -1 ? arr.length : result
}