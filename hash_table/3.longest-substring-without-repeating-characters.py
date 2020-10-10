def lengthOfLongestSubstring(s: str) -> int:

    max = 0


    for i in range(len(s)):
        check_repeat = set()
        curr_text = []
        for j in range(i, len(s)):
            if s[j] not in check_repeat:
                curr_text.append(s[j])
                check_repeat.add(s[j])
                if len(curr_text) > max:
                    max = len(curr_text)
                    max_text = curr_text
            else:
                break

    return max, max_text



print(lengthOfLongestSubstring('ssad'))