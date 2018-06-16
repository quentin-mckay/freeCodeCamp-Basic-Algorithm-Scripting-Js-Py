def truncateString(string, num):
    if len(string) > num:
        return string[:num] + '...'
    return string


# === tests ===
print(truncateString("Peter Piper picked a peck of pickled peppers", 11))
print(truncateString("A-", 1))
print(truncateString("Hello", 20))

    