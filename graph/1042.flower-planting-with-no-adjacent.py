def gardenNoAdj(N, paths):

    color = [1] * N  # N个花园，默认都种1号花
    graph = [[] for i in range(N)]

    print(graph)

    # 把相连的情况写入到数组中，注意只写一次，比如1-2相连，只在2中写与1相连，不在1中重复写与2相连
    for path in paths:
        if path[0] > path[1]:
            graph[path[0] - 1].append(path[1] - 1)
        else:
            graph[path[1] - 1].append(path[0] - 1)

    print(graph)

    for i in range(1, N):  # 注意，这里是从1开始，上面已经默认第一个花园种1号，所以从第二个花园开始分析
        flower = [1, 2, 3, 4]

        print('---------graph: ', i)

        for node in graph[i]:  # 分析每个花园和多少个花园相连，逐个分析它们种了什么花，然后从候选颜色中删除相应的颜色

            print('----------')
            print('node: ', node)

            if color[node] in flower:
                print('color[node]: ', color[node])  # 以第二个花园为例，与第一个花园相连且第一个花园种了一号花，所以节点为1
                flower.remove(color[node])  # 删除候选颜色重的1号
                print('flower: ', flower)
        color[i] = flower[0]  # 把二号花园从默认的1号花改为2号花
        print('color: ', color)

    print(color)
    return color


N = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
gardenNoAdj(N, paths)
