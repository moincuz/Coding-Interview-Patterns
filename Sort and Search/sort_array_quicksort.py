# 20260222
from typing import List
# cursor generated

def sort_array_quicksort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return sort_array_quicksort(left) + middle + sort_array_quicksort(right)

print(sort_array_quicksort([3, 6, 8, 10, 1, 2, 1]))
print(sort_array_quicksort([10, 7, 8, 9, 1, 5]))
print(sort_array_quicksort([1, 2, 3, 4, 5]))
print(sort_array_quicksort([5, 4, 3, 2, 1]))
print(sort_array_quicksort([1, 2, 3, 4, 5]))
#the outcome should be:
#[1, 1, 2, 3, 5, 6, 8, 10]
#[1, 5, 7, 8, 9, 10]
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5]

print("now, this is from them:")


from typing import List


def sort_array(nums: List[int]) -> List[int]:
    quicksort(nums, 0, len(nums) - 1)
    return nums

def quicksort(nums: List[int], left: int, right: int) -> None:
    # Base case: if the subarray has 0 or 1 element, it's already 
    # sorted.
    if left >= right:
        return
    # Partition the array and retrieve the pivot index.
    pivot_index = partition(nums, left, right)
    # Call quicksort on the left and right parts to recursively sort
    # them.
    quicksort(nums, left, pivot_index - 1)
    quicksort(nums, pivot_index + 1, right)

def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[right]
    lo = left
    # Move all numbers less than the pivot to the left, which
    # consequently positions all numbers greater than or equal to the
    # pivot to the right.
    for i in range(left, right):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    # After partitioning, 'lo' will be positioned where the pivot should
    # be. So, swap the pivot number with the number at the 'lo' pointer.
    nums[lo], nums[right] = nums[right], nums[lo]
    return lo

print(sort_array_quicksort([3, 6, 8, 10, 1, 2, 1]))
print(sort_array_quicksort([10, 7, 8, 9, 1, 5]))
print(sort_array_quicksort([1, 2, 3, 4, 5]))
print(sort_array_quicksort([5, 4, 3, 2, 1]))
print(sort_array_quicksort([1, 2, 3, 4, 5]))

#the outcome should be:
#now, this is from them:
#[1, 1, 2, 3, 6, 8, 10]
#[1, 5, 7, 8, 9, 10]
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5]