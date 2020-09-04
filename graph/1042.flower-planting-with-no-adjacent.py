def gardenNoAdj(self, N: int, paths):
    color = [1] * N
    graph = [[] for i in range(N)]
    for path in paths:
        if path[0] > path[1]:
            graph[path[0] - 1].append(path[1] - 1)
        else:
            graph[path[1] - 1].append(path[0] - 1)
    for i in range(1, N):
        flower = [1, 2, 3, 4]
        for node in graph[i]:
            if color[node] in flower:
                flower.remove(color[node])
        color[i] = flower[0]
    return color

