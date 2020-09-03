def longestCommonPrefix(strs):

    # 确定所有单词中最小单词的长度
    if strs==[]:
        return ''

    mini_len = 100
    for i in range(len(strs)):
        if len(strs[i]) < mini_len:
            mini_len = len(strs[i])

    output = ''

    for i in range(mini_len):
        char = strs[0][i]
        all_same = True
        for k in range(len(strs)):
            if strs[k][i] != char:
                all_same = False
                break
        if all_same:
            output += char
        else:
            break

    return output


print(longestCommonPrefix([]))

