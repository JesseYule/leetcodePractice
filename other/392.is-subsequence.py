def isSubsequence(s, t):
    s = list(s)
    t = list(t)
    assit_s = list(s)
    new_j = 0

    for i in range(len(s)):
        for j in range(new_j, len(t)):
            if s[i] == t[j]:
                assit_s.pop(0)
                new_j = j+1
                break

    if len(assit_s) == 0:
        return True
    else:
        return False


print(isSubsequence('abcd', 'abbyyyyyyyyycyyyyyyyyyydyyyyyyyyyyyy'))

