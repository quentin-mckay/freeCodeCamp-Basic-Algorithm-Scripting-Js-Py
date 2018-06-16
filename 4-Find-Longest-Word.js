// ====== My Solution ======
function findLongestWord(str) {
    let wordArray = str.split(' ')
    let longestWord = wordArray[0]
    wordArray.forEach(word => {
      if (word.length > longestWord.length) {
        longestWord = word
      }
    })
    return longestWord.length
  }
  
  
  // ====== Using reduce ======
  function findLongestWordReduce(str) {
    return str.split(' ')
      .reduce((acc, curr) => {
        return Math.max(acc, curr.length)
      }, 0)
  }