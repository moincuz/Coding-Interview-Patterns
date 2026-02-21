from typing import List


def pair_sum_sorted_brute_force(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(pair_sum_sorted_brute_force([2, 7, 11, 15], 9))
print(pair_sum_sorted_brute_force([2, 3, 4], 6))
print(pair_sum_sorted_brute_force([-1, 0], -1))