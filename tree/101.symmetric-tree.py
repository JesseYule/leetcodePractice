# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, left, right):

        # 一定要注意一点，这里的函数会递归调用
        if left is None and right is None:
            return True  # 这里要return true，不是最终的return，而是不断地递归return，这里的true是要告诉上一轮递归，一切情况正常
        if left is None or right is None:
            return False  # 一个为空
        if left.val != right.val:
            return False  # 值不相等 ！！
        # 一下是函数的最终return，也是函数的不断递归，只有函数所有的递归都return true，最终函数才会return true，这里相当于把true一轮轮传递回去
        return self.isSymmetricTree(left.left, right.right) and self.isSymmetricTree(left.right, right.left)
