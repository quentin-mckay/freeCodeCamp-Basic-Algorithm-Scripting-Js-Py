// using map + uppercase
function titleCase(str) {
    return str.toLowerCase().split(' ')
              .map(word => word[0].toUpperCase() + word.slice(1))
              .join(' ')
}

// using regexp
// says "match each first letter after (beginning of string or whitespace"
function titleCase(str) {
    return str.toLowerCase().replace(/(^|\s)(\w)/g, (letter) => letter.toUpperCase())
}

console.log(titleCase("I'm a little tea pot"))