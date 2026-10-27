def reverse_only_letters(s: str):
    arr = [ch for ch in s]
    left = 0
    right = len(s) - 1

    while left < right:
        if arr[left].isalpha() and arr[right].isalpha():
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left].isalpha():
            right -= 1
        elif arr[right].isalpha():
            left += 1
        else:
            left += 1
            right -= 1

    return "".join(arr)


print(
    reverse_only_letters("T4e04uondoenrg93u489573rh348573495h394njf934u394857s6t8")
)  # ==> t4s04ufjnhhrug93r489573ne348573495o394dno934u394857e6T8
