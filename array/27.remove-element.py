def removeElement(nums, val):
    del_num = 0
    for i in range(len(nums)):
        index = i - del_num
        if nums[index] == val:
            del nums[index]
            del_num += 1

    return len(nums)


nums = [3, 2, 2, 3]
print(removeElement(nums, 2))

