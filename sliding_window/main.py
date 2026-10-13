def maximum_length_substring(s: str):
    left, right = 0, 0
    max_count = 1
    global counter
    counter = {}

    counter[s[0]] = 1

    while right < len(s) - 1:
        right += 1
        if counter.get(s[right]):
            counter[s[right]] += 1
        else:
            counter[s[right]] = 1

        while counter[s[right]] == 3:
            counter[s[left]] -= 1
            left += 1

        max_count = max(max_count, right - left + 1)

    return max_count


print(maximum_length_substring(input("Type something: ")))
print(counter)
