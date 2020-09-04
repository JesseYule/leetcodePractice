
def nextGreaterElement(nums1, nums2):

    equal_index = [-1] * len(nums1)
    result = [-1] * len(nums1)
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                equal_index[i] = j
            if equal_index[i] != -1 and nums2[j] > nums1[i]:
                result[i] = nums2[j]
                break

    return result


nums1 = [4, 1, 2]
nums2 = [1, 2, 3, 4]

print(nextGreaterElement(nums1, nums2))

# [-1,2,3]