def intersection_of_two_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))


print(intersection_of_two_arrays([1, 2, 3, 4], [1, 2, 2, 5]))
