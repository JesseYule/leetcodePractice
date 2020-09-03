def romanToInt(s):

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
             "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    s = list(s)

    reverse_index = -1
    output = 0

    for i in range(len(s)):
        if len(s) == 2 and roman[s[-2]] < roman[s[-1]]:
            # 考虑IV、IX这些特殊情况
            output += roman[s[-2] + s[-1]]
            # print(roman[s[-2] + s[-1]])
            break
        elif reverse_index == -1 * len(s):
            # 考虑当index来到起点时如何处理
            output += roman[s[0]]
            # print(roman[s[0]])
            break
        elif roman[s[reverse_index - 1]] >= roman[s[reverse_index]]:
            # 字母从大到小正常排列时的情况
            output += roman[s[reverse_index]]
            reverse_index -= 1
            # print(roman[s[reverse_index]])
        else:
            # 字母特殊情况，也就是IV、IX等
            special_combination = s[reverse_index - 1] + s[reverse_index]
            output += roman[special_combination]
            reverse_index -= 2
            i += 1
            # print(roman[special_combination])
            if -1 * reverse_index > len(s):
                break

    return output
