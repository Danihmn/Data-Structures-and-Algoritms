def contains_duplicate(arr) -> bool:
    seen_items = set()

    for i in arr:
        if i in seen_items:
            return True
        seen_items.add(i)
    return False


print(contains_duplicate("ABCDE"))  # ==> False
print(contains_duplicate("ABCDA"))  # ==> True
