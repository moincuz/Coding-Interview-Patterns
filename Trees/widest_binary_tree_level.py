# 20260221  not runnable because of  'ds'. fixed in balanced_binary_tree_validation.py check there

from collections import deque
from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""


def widest_binary_tree_level(root: TreeNode) -> int:
    if not root:
        return 0
    max_width = 0
    queue = deque([(root, 0)])  # Stores (node, index) pairs.
    while queue:
        level_size = len(queue)
        # Set the 'leftmost_index' to the index of the first node in 
        # this level. Start 'rightmost_index' at the same point as 
        # 'leftmost_index' and update it as we traverse the level, 
        # eventually positioning it at the last node.
        leftmost_index = queue[0][1]
        rightmost_index = leftmost_index
        # Process all nodes at the current level.
        for _ in range(level_size):
            node, i = queue.popleft()
            if node.left:
                queue.append((node.left, 2*i + 1))
            if node.right:
                queue.append((node.right, 2*i + 2))
            rightmost_index = i
        max_width = max(max_width, rightmost_index - leftmost_index + 1)
    return max_width

print(widest_binary_tree_level(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))))
