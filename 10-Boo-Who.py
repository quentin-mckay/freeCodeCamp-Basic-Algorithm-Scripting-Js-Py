def booWho(val):
    return type(val) is bool


# === tests ===
print(booWho(True))
print(booWho(False))
print(booWho([1, 2, 3]))