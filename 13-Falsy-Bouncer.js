function bouncer(arr) {
    return arr.filter(val => val)
}


// === tests ===
console.log(bouncer([false, null, 0, NaN, undefined, ""]))  // => [] (all falsy)

// note: [] is truthy in JS, but [] is falsy in Python
