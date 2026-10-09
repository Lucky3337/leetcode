from idlelib.tree import TreeNode
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def gather_values(node: Optional[TreeNode]):
            if not node:
                return
            result.append(node.val)
            gather_values(node.left)
            gather_values(node.right)

        gather_values(root)
        return result