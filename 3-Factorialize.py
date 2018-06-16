# using for loop
def factorialize(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total

# using recursion
def factorialize(num):
    if num <= 1: 
        return 1
    else: 
        return num * factorialize(num - 1)


# === tests ===
print(factorialize(0))
print(factorialize(5))