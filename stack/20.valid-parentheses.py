def isValid(s):

    mapping = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}
    right_bracket = {')', ']', '}'}
    left_bracket = {'(', '[', '{'}

    result = []

    left_bracket_num = 0

    # 考虑没有左括号的特殊情况
    for i in range(len(list(s))):
        if s[i] in left_bracket:
            left_bracket_num += 1

    if left_bracket_num == 0:
        return False

    # 考虑第一个就是右括号的特殊情况
    if s[0] in right_bracket:
        return False

    for i in range(len(s)):
        if s[i] in left_bracket:
            # 遇到左括号就添加到stack中
            result.append(s[i])
            # print(i, result)
        elif s[i] in right_bracket and len(result) > 0 and mapping[s[i]] == result[-1]:
            # 遇到右括号，然后又可以和上一个符号匹配的，就删除stack中最后的符号
                result.pop()
                # print(i, result)
        else:
            # 否则，就意味着遇到一个右括号，又没办法和stack最后的符号匹配，这种情况肯定错的，所以直接return结果
            return False

    if len(result) > 0:
        output = False
    else:
        output = True

    return output


print(isValid('(])'))
