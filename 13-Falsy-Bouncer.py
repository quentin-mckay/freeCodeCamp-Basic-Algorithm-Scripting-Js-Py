def bouncer(lst):
    return [val for val in lst if val]


# === tests ===
print(bouncer([7, "ate", "", False, 9]))
print(bouncer([False, None, 0, "", []]))  # => []  (all falsy!)

# note: [] is truthy in JS, but [] is falsy in Python