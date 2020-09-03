def reverse(x):
    negative = 1

    if x < 0:
        x = x * -1
        negative = -1

    x = str(x)
    output = ''

    for i in range(len(x)):
        element = x[-i-1]
        output += element

    output = int(output) * negative

    if output < -2**31 or output > 2**31 - 1:
        output = 0

    return output
