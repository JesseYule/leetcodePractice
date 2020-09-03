def isPalindrome(x):
    x = str(x)
    output = True
    reverse_index = -1

    for i in range(len(x) // 2 + 1):
        if x[i] != x[reverse_index]:
            output = False
            break
        reverse_index -= 1

    return output
