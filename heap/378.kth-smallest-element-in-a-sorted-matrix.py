import heapq


def kthSmallest(matrix, k):
    n = len(matrix)
    pq = [(matrix[i][0], i, 0) for i in range(n)]
    print(pq)
    heapq.heapify(pq)

    ret = 0
    for i in range(k - 1):
        num, x, y = heapq.heappop(pq)
        if y != n - 1:
            heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

    return heapq.heappop(pq)[0]


matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

k = 8

print(kthSmallest(matrix, k))