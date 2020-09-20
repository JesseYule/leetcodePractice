def calPoints(ops):

    point = []

    for i in range(len(ops)):

        if ops[i] == 'C':
            point.pop()
            pass
        elif ops[i] == 'D':
            point.append(int(point[-1]) * 2)
            pass
        elif ops[i] == '+':
            point.append(int(point[-1]) + int(point[-2]))
            pass
        else:
            point.append(int(ops[i]))

    return sum(point)


ops = ["5","-2","4","C","D","9","+","+"]

print(calPoints(ops))
