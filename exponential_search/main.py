def binary_search(array, *, left, right, n):
    while left < right:
        mid = int((left + right) / 2)
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            left = mid + 1
        else:
            right = mid
    return -1


def exponential_search(array, n):
    if array[0] == n:
        return 0

    arraylen = len(array)
    i = 1

    while i < arraylen and array[0] < n:
        i *= 2
        if array[i] == n:
            return i

    return binary_search(array, left=array[i // 2], right=min(i, arraylen - 1), n=n)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(exponential_search(array, 5))
