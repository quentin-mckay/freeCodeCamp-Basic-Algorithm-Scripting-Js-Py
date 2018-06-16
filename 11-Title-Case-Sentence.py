def titleCase(string):
    list_of_words = string.split()
    list_of_capitalized_words = [word[0].upper() + word[1:] for word in list_of_words]
    return ' '.join(list_of_capitalized_words)


# single line version
def titleCase(string):
    return ' '.join([(word[0].upper() + word[1:]) for word in string.split()])


# === tests ===
print(titleCase("I'm a little tea pot"))