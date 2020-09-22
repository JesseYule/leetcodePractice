import collections


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []

        result = [[root.val]]
        queue = [root]
        assit_result = []

        while queue:

            len_queue = len(queue)

            for i in range(len_queue):
                curr_node = queue.pop(0)

                if curr_node.left:
                    assit_result.append(curr_node.left.val)
                    queue.append(curr_node.left)
                if curr_node.right:
                    assit_result.append(curr_node.right.val)
                    queue.append(curr_node.right)

            result.append(assit_result)
            assit_result = []

        del result[-1]
        result = list(reversed(result))

        return result


# 广度优先搜索，过程和我一样
class Solution:
    def levelOrderBottom(self, root):
        levelOrder = list()
        if not root:
            return levelOrder

        q = collections.deque([root])
        while q:
            level = list()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)

        return levelOrder[::-1]
