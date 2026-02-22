# 20260222
import heapq
from typing import List


def kth_largest_integer_min_heap(nums: List[int], k: int) -> int:
    min_heap = []
    heapq.heapify(min_heap)
    for num in nums:
        # Ensure the heap has at least 'k' integers.
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        # If 'num' is greater than the smallest integer in the heap, pop
        # off this smallest integer from the heap and push in 'num'.
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]

print(kth_largest_integer_min_heap([3, 2, 1, 5, 6, 4], 2))
print(kth_largest_integer_min_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(kth_largest_integer_min_heap([1], 1))
print(kth_largest_integer_min_heap([1, 2], 2))
print(kth_largest_integer_min_heap([1, 2, 3], 3))
print(kth_largest_integer_min_heap([1, 2, 3, 4], 4))
print(kth_largest_integer_min_heap([1, 2, 3, 4, 5], 5))

#the output is 5
