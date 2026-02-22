#20260221


from typing import List


def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    stack = []
    # Find the next largest number of each element, starting with the 
    # rightmost element.
    for i in range(len(nums) - 1, -1, -1):
        # Pop values from the top of the stack until the current 
        # value's next largest number is at the top.
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        # Record the current value's next largest number, which is at 
        # the top of the stack. If the stack is empty, record -1.
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res

print(next_largest_number_to_the_right([2, 1, 2, 4, 3]))
print(next_largest_number_to_the_right([1, 2, 3, 4, 5]))
print(next_largest_number_to_the_right([5, 4, 3, 2, 1]))
print(next_largest_number_to_the_right([1, 1, 1, 1, 1]))
print(next_largest_number_to_the_right([1, 2, 3, 4, 5]))
print(next_largest_number_to_the_right([5, 4, 3, 2, 1]))
print(next_largest_number_to_the_right([1, 1, 1, 1, 1]))

## outcome should be:
# [4, 2, 4, -1, 4]
# [5, 4, 3, 2, 1]
# [-1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1]