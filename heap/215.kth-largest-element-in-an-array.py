import heapq


def findKthLargest(nums, k):
    h = []
    for value in nums:
        heapq.heappush(h, value)

    result = [heapq.heappop(h) for i in range(len(h))]

    return result[-k]


nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(findKthLargest(nums, -3))


