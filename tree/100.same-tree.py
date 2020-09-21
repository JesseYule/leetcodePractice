import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(root):
            if not root:
                return [None]
            else:
                return [root.val] + preorder(root.left) + preorder(root.right)

        return preorder(p) == preorder(q)


# 这个算法很高明，把所有节点都打印成列表，然后判断两个列表是否相等，算法复杂度为O(n)


# 深度优先搜索
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # 前面判断空与非空的情况，只有两个都非空才需要递归分析
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:  # 对比value
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 广度优先搜索
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2



# 二叉树有两种解法，一种是遍历所有节点，一种是根据需要中途退出

# void plusOne(TreeNode root) {
#     if (root == null) return;
#     root.val += 1;
#
#     plusOne(root.left);
#     plusOne(root.right);
# }

# 比如这个就是通过递归遍历所有节点进行分析，遍历的思路就在于递归当前节点的左右子节点，比如把树中每个节点都加1这类操作

# boolean isSameTree(TreeNode root1, TreeNode root2) {
#     // 都为空的话，显然相同
#     if (root1 == null && root2 == null) return true;
#     // 一个为空，一个非空，显然不同
#     if (root1 == null || root2 == null) return false;
#     // 两个都非空，但 val 不一样也不行
#     if (root1.val != root2.val) return false;
#
#     // root1 和 root2 该比的都比完了
#     return isSameTree(root1.left, root2.left)
#         && isSameTree(root1.right, root2.right);
# }

# 以上是检查两棵树是否完全相等，当发现有子节点不相等，直接可以return，不需要遍历完整棵树


