import collections


# 自己的思路，主要问题是太慢
def frequencySort(s):

    count = collections.Counter(s)

    str = list(count)
    freq = list(count.values())

    countlist = []
    for i in range(len(str)):
        countlist.append([freq[i], str[i]])

    countlist.sort(reverse=True)

    output = ""

    for i in range(len(countlist)):
        for j in range(int(countlist[i][0])):
            output += countlist[i][1]

    return output


print(frequencySort("tree"))
