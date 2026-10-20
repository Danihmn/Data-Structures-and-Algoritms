def subarray_sum(nums: list, k: int) -> int:
    count = 0
    prefix_sum = 0
    freq = {}
    freq[0] = 1

    for num in nums:
        prefix_sum += num
        count + freq[prefix_sum - k]
        freq[prefix_sum] += 1

    return count
