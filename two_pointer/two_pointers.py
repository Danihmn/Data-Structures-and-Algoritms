def reverse_words(phrase: str):
    result_str = ""
    left, right = 0, 0

    while right < len(phrase):
        if phrase[right] != " ":
            right += 1
        else:
            result_str += phrase[left:right + 1][::-1]
            right += 1
            left = right

    result_str += " "
    result_str += phrase[left:right + 2][::-1]
    return result_str[1:]

print(reverse_words("hello world")) # Output: 'olleh dlrow'