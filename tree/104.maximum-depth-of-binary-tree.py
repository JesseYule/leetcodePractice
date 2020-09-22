# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归的思路比较通用，注意max的应用
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


# 广度优先
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = [(1, root)]  # queue储存了层数和节点，这是他高明的地方
        while queue:
            depth, node = queue.pop(0)
            if node.left:  # 如果有左节点，在增加左节点的同时增加层数
                queue.append((depth+1,node.left))
            if node.right:
                queue.append((depth+1,node.right))
        return depth
