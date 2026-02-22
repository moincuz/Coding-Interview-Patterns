#20260221


from collections import deque
from typing import List


def maximums_of_sliding_window(nums: List[int], k: int) -> List[int]:
    res = []
    dq = deque()
    left = right = 0
    while right < len(nums):
        # 1) Ensure the values of the deque maintain a monotonic decreasing order
        # by removing candidates <= the current candidate.
        while dq and dq[-1][0] <= nums[right]:
            dq.pop()
        # 2) Add the current candidate.
        dq.append((nums[right], right))
        # If the window is of length 'k', record the maximum of the window.
        if right - left + 1 == k:
            # 3) Remove values whose indexes occur outside the window.
            if dq and dq[0][1] < left:
                dq.popleft()
            # The maximum value of this window is the leftmost value in the 
            # deque.
            res.append(dq[0][0])
            # Slide the window by advancing both 'left' and 'right'. The right  
            # pointer always gets advanced so we just need to advance 'left'.
            left += 1
        right += 1
    return res

print(maximums_of_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maximums_of_sliding_window([1], 1))
print(maximums_of_sliding_window([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(maximums_of_sliding_window([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3))
print(maximums_of_sliding_window([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3))
print(maximums_of_sliding_window([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(maximums_of_sliding_window([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1))
print(maximums_of_sliding_window([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))

## outcome should be:
# [3, 3, 5, 5, 6, 7]
# [1]
# [3, 4, 5, 6, 7, 8, 9, 10]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]