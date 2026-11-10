class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        values = []
        def move(node: TreeNode | None):
            if not node:
                return
            move(node.left)
            move(node.right)
            values.append(node.val)
        move(root)
        return values


if __name__ == "__main__":
    solution = Solution()
    print(solution)