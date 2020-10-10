# 主要总结DFS和BFS在树的应用

# ----------------------------DFS例子--------------------------------
class Graph(object):

    # 这里构建了无向图，不是树，有节点和边

    def __init__(self):
        self.node_neighbors = {}  # 通过字典指名node与什么相连
        self.visited = set()  # 通过set储存访问过的节点，一方面作为输出，另一方面避免重复访问处理

    def add_nodes(self, nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []  # 初始化数组，用来储存连接的node

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):  # 确定uv之前没有相互连接
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)  # 储存节点的时候，既要储存u连接v，也要储存v连接u

    def nodes(self):
        return self.node_neighbors.keys()

    '''
    DFS伪代码，一般通过递归访问左右节点实现
    def DFS(A):
        if(A不合法)
            return;
        if(A为目标状态)
            输出或记录路径
        if(A不为目标状态)
            dfs(A.left) 
            dfs(A.right) 
    '''

    def depth_first_search(self, root=None):
        order = []

        def dfs(node):  # 在def中内嵌def，感觉这种写法不是很好
            self.visited.add(node)  # 把访问过的节点追加到visited中
            order.append(node)  # 对node进行分析
            for n in self.node_neighbors[node]:  # 这里是重点，访问子节点
                if n not in self.visited:
                    dfs(n)  # 通过迭代，实现深度优先搜索

        if root:
            dfs(root)  # 从root开始访问

        # 对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
        for node in self.nodes():
            if node not in self.visited:
                dfs(node)

        self.visited = set()  # 完成处理后清空set，避免重复调用函数时出错
        return order


if __name__ == '__main__':

    g = Graph()

    g.add_nodes([i + 1 for i in range(8)])

    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))

    print("nodes:", g.nodes())

    result = g.depth_first_search(1)

    print(result)



# ----------------------------------BFS例子------------------------------------

from collections import deque  # collections 模块提供了一些有用的集合类

# 这一题是找出图中所有名字最后一位字母是‘m’的人

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = ['tom']

# 这个图里'you'就是根节点

print(graph)


def person_is_seller(name):  # 名字最后一位字母是‘m’就是商人
    return name[-1] == 'm'


'''
BFS要建一个辅助的队列进行分析，带访问的节点入队，通过先进先出获取当前要访问的节点
def BFS(root):
    queue = []
    queue.add(root)
    while queue is not None:
        node = queue.pop(0)
        analyse(node)
        if node.left:
            queue.add(queue.left)
        if node.right:
            queue.add(queue.left)
        
'''

def search(root):
    search_queue = deque()  # 建立一个双端队列
    search_queue += graph[root]  # 传入树的根节点
    searched = []  # 这个数组用于记录检查过的人

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:  # 仅当这个人没被检查过时才检查，这是为了提高效率
            if person_is_seller(person):  # 判断节点是否为搜索目标
                print(person + ' is a mango seller!')
            else:  # 如果person不是商人，就将person的朋友都加入搜索队列
                search_queue += graph[person]
                searched.append(person)  # 将这个人标记为检查过


search('you')