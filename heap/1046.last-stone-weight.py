def lastStoneWeight(stones):

    while len(stones) > 1:
        stones.sort(key=None, reverse=True)
        max1 = stones.pop(0)
        max2 = stones.pop(0)
        if max1 != max2:
            stones.append(abs(max1-max2))

    if len(stones) == 0:
        result = 0
    else:
        result = stones[0]

    return result


stones = [2,2]
print(lastStoneWeight(stones))