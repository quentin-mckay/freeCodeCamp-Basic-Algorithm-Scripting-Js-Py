# very nice !!
def chunkArrayInGroups(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]


# === tests ===
print(chunkArrayInGroups(["a", "b", "c", "d"], 2))
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3))
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4))