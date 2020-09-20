def isIsomorphic(s, t):

    dict = {}

    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = t[i]
        else:
            if dict[s[i]] != t[i]:
                return False

    dict = {}

    for i in range(len(t)):
        if t[i] not in dict:
            dict[t[i]] = s[i]
        else:
            if dict[t[i]] != s[i]:
                return False

    return True


s = 'ab'
t = 'aa'

print(isIsomorphic(s, t))
