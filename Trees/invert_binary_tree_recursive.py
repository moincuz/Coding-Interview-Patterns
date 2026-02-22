# 20260221  not runnable because of  'ds'. fixed in balanced_binary_tree_validation.py check there

from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""


def invert_binary_tree_recursive(root: TreeNode) -> TreeNode:
    # Base case: If the node is null, there's nothing to invert.
    if not root:
        return None
    # Swap the left and right subtrees of the current node.
    root.left, root.right = root.right, root.left
    # Recursively invert the left and right subtrees.
    invert_binary_tree_recursive(root.left)
    invert_binary_tree_recursive(root.right)
    return root

print(invert_binary_tree_recursive(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))))
