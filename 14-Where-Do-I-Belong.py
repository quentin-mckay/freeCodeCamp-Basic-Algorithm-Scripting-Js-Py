def getIndexToIns(lst, num):
    for index, value in enumerate(sorted(lst)):
        if num <= value:
            return index
    return len(lst)


# === tests ===
print(getIndexToIns([10, 20, 30, 40, 50], 35)) # => 3
print(getIndexToIns([10, 20, 30, 40, 50], 30)) # => 2
print(getIndexToIns([], 1)) # => 0