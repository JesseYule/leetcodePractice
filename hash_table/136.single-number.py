
# 使用集合存储数字

def singleNumber(nums):

    candidate = set()

    for i in range(len(nums)):
        if nums[i] in candidate:
            candidate.remove(nums[i])
        else:
            candidate.add(nums[i])

    print(candidate)

    candidate = list(candidate)

    return candidate[0]


# 使用哈希表
def singleNumber2(nums):


    candidate = {}

    for i in range(len(nums)):
        candidate[nums[i]] = 0

    for i in range(len(nums)):
        if nums[i] in candidate:
            candidate[nums[i]] += 1

    print(candidate)

    for i in range(len(nums)):
        if candidate[nums[i]] == 1:
            print(nums[i])
            return nums[i]


nums = [4,1,2,1,2]
singleNumber2(nums)