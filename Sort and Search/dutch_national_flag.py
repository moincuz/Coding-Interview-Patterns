# 20260222

from typing import List


def dutch_national_flag(nums: List[int]) -> None:
    i, left, right = 0, 0, len(nums) - 1
    while i <= right:
        # Swap 0s with the element at the left pointer.
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        # Swap 2s with the element at the right pointer.
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1

print(dutch_national_flag([2, 0, 2, 1, 1, 0]))
print(dutch_national_flag([2, 0, 1]))
print(dutch_national_flag([0, 1, 2]))
print(dutch_national_flag([0, 2, 1]))
print(dutch_national_flag([2, 0, 1]))
print(dutch_national_flag([0, 2, 1]))

#the output is [0, 0, 1, 1, 2, 2]