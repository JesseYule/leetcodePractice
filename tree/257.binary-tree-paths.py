import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 深度优先搜索
class Solution:
    def binaryTreePaths(self, root):

        def construct_paths(root, path):
            if root:  # 注意，有可能传入None，所以要判断一下root是不是None
                path += str(root.val)
                if not root.left and not root.right:  # 如果当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths


# 广度优先搜索
class Solution:
    def binaryTreePaths(self, root):
        paths = list()
        if not root:
            return paths

        # 双向队列deque
        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            # 当还有子节点

            # popleft（获取最左边的一个元素，并在队列中删除）
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:  # 当没有了任何子节点
                paths.append(path)
            else:  # 如果还有子节点
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))

                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))

        return paths
