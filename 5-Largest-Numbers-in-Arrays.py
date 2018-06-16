# accepts any number of subarrays
def largestOfSubs(array):
    return [max(subarray) for subarray in array]


# === tests ===
test = [[4, 5, 1, 3], 
        [13, 27, 18, 26], 
        [32, 35, 37, 39], 
        [1000, 1001, 857, 1]]
print(largestOfSubs(test))
