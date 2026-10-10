def binary_search(nums, target):
    left_pointer = 0
    right_pointer = len(nums)
    steps = 0
    while left_pointer < right_pointer:
        steps += 1
        mid = int((left_pointer + right_pointer) / 2)

        if nums[mid] == target:
            print("Step: ", steps)
            return mid
        elif nums[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid
    return -1

print(binary_search([1, 2, 3, 4, 5, 6], 6))