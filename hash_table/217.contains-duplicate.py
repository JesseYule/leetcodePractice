def containsDuplicate(nums):

    numset = set()

    for i in range(len(nums)):
        if nums[i] not in numset:
            numset.add(nums[i])
        else:
            return True

    return False


print(containsDuplicate([1,2,3,4,1]))

# 也可以用字典做，出现过的为1，否则为0，当检测到当前数字对应的value为1，直接return false
