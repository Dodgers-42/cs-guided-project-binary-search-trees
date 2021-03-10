"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(self):
    if self.left is None and self.right is None:
        return 1
    left_height = 0
    right_height = 0
    if self.left is not None:
        left_height = self.left.maxDepth()
    if self.right is not None:
        right_height = self.right.maxDepth()

    max_depth = max(left_height, right_height)
    return max_depth + 1



root = BinaryTreeNode(8)

root.insert(5)
root.insert(11)
root.insert(2)
root.insert(7)
root.insert(10)
root.insert(12)
root.insert(6)

print(root.search(15))

print(root.find_minimum_value())