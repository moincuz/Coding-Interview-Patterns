
from typing import List


def shift_zeros_to_the_end_naive(nums: List[int]) -> None:
    temp = [0] * len(nums)
    i = 0
    # Add all non-zero elements to the left of 'temp'.
    for num in nums:
        if num != 0:
            temp[i] = num
            i += 1
    # Set 'nums' to 'temp'.
    for j in range(len(nums)):
        nums[j] = temp[j]

print(shift_zeros_to_the_end_naive([0, 1, 0, 3, 12]))
print(shift_zeros_to_the_end_naive([0]))
print(shift_zeros_to_the_end_naive([1]))
print(shift_zeros_to_the_end_naive([0, 0, 0, 0, 0]))
print(shift_zeros_to_the_end_naive([1, 0, 1, 0, 1]))
print(shift_zeros_to_the_end_naive([0, 1, 0, 1, 0]))
print(shift_zeros_to_the_end_naive([0, 1, 0, 1, 0]))