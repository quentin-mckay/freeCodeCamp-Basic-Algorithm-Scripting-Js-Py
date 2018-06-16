// for loop way
function chunkArrayInGroups(arr, size) {
    let arrCopy = Array.from(arr)  // make a copy so we don't alter the original
    const finalArray = []
    for (let i = 0; i < arrCopy.length; i += size) {
        finalArray.push(arrCopy.slice(i, i+size))
    }
    return finalArray
}


// using Array(), Math.ceil(), and map  (not mine)
const chunkArrayInGroups = (arr, size) =>
  [...Array(Math.ceil(arr.length / size))].map((val, i) =>
    arr.slice(i * size, (i + 1) * size))


// ====== neat ways to create Arrays (like above example) ======
// both of these create array like [0, 1, 2, 3, 4, ...]
let test = [...Array(4)].map((val, i) => i)
test = [...Array(10).keys()]


let used

