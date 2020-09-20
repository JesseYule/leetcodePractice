def isHappy(n):

    n = list(str(n))

    appear_val = set()

    sum = 0

    while sum != 1:

        sum = 0
        for i in range(len(n)):
            sum += int(n[i])**2
        n = list(str(sum))

        # 一直迭代，结果等不等于1
        if sum == 1:
            return True
        elif sum in appear_val:  # 如果数值重复出现，那就证明无限循环
            return False
        else:  # 否则把计算的结果加入到集合中
            appear_val.add(sum)


# 哈希表解法，和集合感觉差不多

def isHappy(n):
    if (n == 1):
        return True

    seen = {}  # 这里用集合好像效果也差不多

    def sumDigit(n: int) -> int:
        res = 0
        while(n != 0):
            res += (n % 10) ** 2
            n = n // 10
        return res

    while(n not in seen):
        seen[n] = True
        n = sumDigit(n)
        if (n == 1):
            return True

    return False


print(isHappy(19))