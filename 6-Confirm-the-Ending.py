# using slices
def confirmEnding(string, target):
    return string[-len(target):] == target


# === tests ===
print(confirmEnding("Bastian", "n"))
print(confirmEnding("Congratulation", "on"))
print(confirmEnding("Open sesame", "pen"))