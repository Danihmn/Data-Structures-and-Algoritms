def first_unique_character_in_string(array):
    seen = {}
    for char in array:
        seen[char] = seen.get(char, 0) + 1

    for index, char in enumerate(array):
        if seen[char] == 1:
            return index

    return -1


print(first_unique_character_in_string(["t", "T"]))
