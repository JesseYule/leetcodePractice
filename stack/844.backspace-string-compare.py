def backspaceCompare(S, T):

    def deleteBackspace(str):
        stack_str = []
        for i in range(len(str)):
            if len(stack_str) > 0 and str[i] == '#':
                stack_str.pop()
            elif len(stack_str) == 0 and str[i] == '#':
                pass
            else:
                stack_str.append(str[i])

        return stack_str

    S = deleteBackspace(S)
    T = deleteBackspace(T)
    print(S)
    print(T)

    return S == T



S = "y#fo##f"
T = "y#f#o##f"
print(backspaceCompare(S, T))
