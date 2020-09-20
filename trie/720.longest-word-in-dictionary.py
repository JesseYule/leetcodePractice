
# 暴力解法

def longestWord(words):

    candidate = set(words)

    outputs = set()

    for i in range(len(words)):
        word_len = len(words[i])
        outputs.add(words[i])
        for k in range(word_len):
            if words[i][0:k+1] not in candidate:
                outputs.remove(words[i])
                break

    outputs = list(outputs)
    print(outputs)

    max_len = 0

    final_output = []

    for i in range(len(outputs)):
        if len(outputs[i]) >= max_len:
            final_output.append(outputs[i])
            max_len = len(outputs[i])

    max_len = 0
    for i in range(len(final_output)):
        if len(final_output[i]) > max_len:
            max_len = len(final_output[i])

    final_result = set()
    for i in range(len(final_output)):
        if len(final_output[i]) == max_len:
            final_result.add(final_output[i])

    final_result = list(final_result)

    return min(final_result)


words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
longestWord(words)
