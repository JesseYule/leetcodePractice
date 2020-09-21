import heapq


def nthUglyNumber(n: int) -> int:
    heap = []
    heapq.heappush(heap, 1)

    seen = set()
    seen.add(1)

    factors = [2, 3, 5]  # 新的丑数只会是当前的丑数乘以2、3、5

    curr_ugly = 1

    for _ in range(n):
        curr_ugly = heapq.heappop(heap)  # 取出n次最小堆，第n次就是第n个丑数
        for f in factors:
            new_ugly = curr_ugly * f
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)  # 这里只是把丑数push到堆中
    return curr_ugly


print(nthUglyNumber(10))
