# loop through second string and return False 
# as soon as a letter isn't in the first string
# otherwise return True
def mutation(lst):
    string1 = lst[0].lower()
    string2 = lst[1].lower()
    
    for letter in string2:
        if letter not in string1:
            return False
    
    return True

# using all() and list comprehension (prob less efficient then other solution)
# create list of True/False's from testing each letter of string2 against string1 
# and check whether they're all True
def mutation(lst):
    return all([(letter in lst[0].lower()) for letter in lst[1].lower()])
        

# === tests ===
print(mutation(['hello', 'hey']))
print(mutation(["hello", "Hello"]))
print(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]))
print(mutation(["Mary", "Aarmy"]))
print(mutation(["hello", "neo"]))