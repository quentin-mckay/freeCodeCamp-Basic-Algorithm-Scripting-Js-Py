def findElement(lst, func):
    for el in lst:
        if func(el): return el



# === tests ===
print(findElement([1,3,5,8,9,10], lambda x: x % 2 == 0))
print(findElement(['apple', 'banana', 'fig'], lambda x: len(x) == 3))