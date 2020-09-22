# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 深度优先搜索
class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        if not root.left and not root.right:  # 到达最低端就返回1
            return 1

        min_depth = 10 ** 9  # 起始的对比，详见下方

        # 分析最小值不能像分析最大值那样对比left和right，因为只有n个左节点的情况下，算法会认为深度为1，但实际上深度为n

        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)

        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1


import collections


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        que = collections.deque([(root, 1)])  # 广度优先中把节点和深度绑在一起是一个很常用且高明的操作
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:  # 一检测出空节点就知道此时的深度为最小深度，所以广度优先更好理解
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return 0
