
# 递归
class Solution:
    def isBalanced(self, root):

        def height(root):
            if root is None:
                return 0
            else:
                left_height = height(root.left)
                right_height = height(root.right)
                return max(left_height, right_height) + 1

        if not root:
            return True

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

