def frankenSplice(list1, list2, n):
    result = list2.copy()
    result[n:n] = list1
    return result


# === tests ===
print(frankenSplice([1,2,3], [4,5], 1))
print(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2))