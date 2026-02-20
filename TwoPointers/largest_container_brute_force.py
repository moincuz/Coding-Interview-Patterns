
from typing import List


def largest_container_brute_force(heights: List[int]) -> int:
    n = len(heights)
    max_water = 0
    # Find the maximum amount of water stored between all pairs of
    # lines.
    for i in range(n):
        for j in range(i + 1, n):
            water = min(heights[i], heights[j]) * (j - i)
            max_water = max(max_water, water)
    return max_water

print(largest_container_brute_force([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(largest_container_brute_force([1, 1]))
print(largest_container_brute_force([4, 3, 2, 1, 4]))
print(largest_container_brute_force([1, 2, 1]))