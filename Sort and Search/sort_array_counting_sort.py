# 20260222
# cursor generated
from typing import List


def sort_array_counting_sort(nums: List[int]) -> List[int]:
    max_num = max(nums)
    min_num = min(nums)
    range_of_elements = max_num - min_num + 1
    count_array = [0] * range_of_elements
    output_array = [0] * len(nums)
    for num in nums:
        count_array[num - min_num] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    for i in range(len(nums) - 1, -1, -1):
        output_array[count_array[nums[i] - min_num] - 1] = nums[i]
        count_array[nums[i] - min_num] -= 1
    return output_array

print(sort_array_counting_sort([4, 2, 2, 8, 3, 3, 1]))
print(sort_array_counting_sort([1, 4, 1, 2, 7, 5, 2]))
print(sort_array_counting_sort([1, 2, 3, 4, 5]))
print(sort_array_counting_sort([5, 4, 3, 2, 1]))
print(sort_array_counting_sort([1, 2, 3, 4, 5]))

print("now, this is from them:")

from typing import List


def sort_array_counting_sort(nums: List[int]) -> List[int]:
    if not nums:
        return []
    res = []
    # Count occurrences of each element in 'nums'.
    counts = [0] * (max(nums) + 1)
    for num in nums:
        counts[num] += 1
    # Build the sorted array by appending each index 'i' to it a total 
    # of 'counts[i]' times.
    for i, count in enumerate(counts):
        res.extend([i] * count)
    return res

print(sort_array_counting_sort([4, 2, 2, 8, 3, 3, 1]))
print(sort_array_counting_sort([1, 4, 1, 2, 7, 5, 2]))
print(sort_array_counting_sort([1, 2, 3, 4, 5]))
print(sort_array_counting_sort([5, 4, 3, 2, 1]))
print(sort_array_counting_sort([1, 2, 3, 4, 5]))