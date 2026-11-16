# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root.left and not root.right:
            return [str(root.val)]

        temp_values = []
        result = []

        def healper(root):
            temp_values.append(str(root.val))
            if not root.left and not root.right:
                result.append("->".join(temp_values))
            else:
                if root.left:
                    healper(root.left)
                if root.right:
                    healper(root.right)
            temp_values.pop()

        healper(root)
        return result


if __name__ == '__main__':
    head = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    solution = Solution()
    print(solution.binaryTreePaths(head))
    print("--".join(["1","2","3"]))