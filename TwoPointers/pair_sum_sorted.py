
from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        # If the sum is smaller, increment the left pointer, aiming
        # to increase the sum toward the target value.
        if sum < target:
            left += 1
        # If the sum is larger, decrement the right pointer, aiming
        # to decrease the sum toward the target value.
        elif sum > target:
            right -= 1
        # If the target pair is found, return its indexes.
        else:   
            return [left, right]
    return []

print(pair_sum_sorted([2, 7, 11, 15], 9))
print(pair_sum_sorted([2, 3, 4], 6))
print(pair_sum_sorted([-1, 0], -1))