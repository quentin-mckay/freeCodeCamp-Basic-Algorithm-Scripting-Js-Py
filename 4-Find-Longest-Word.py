# using list comprehension
def findLongestWord(string):
    word_array = string.split()  # uses whitespace as default
    lengths_array = [len(word) for word in word_array]
    return max(lengths_array)

# in one line
def findLongestWord(string):
    return max([len(word) for word in string.split()])


# === tests ===
print(findLongestWord("The quick brown fox"))