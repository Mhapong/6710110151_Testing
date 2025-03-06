def Staircase(num):
    result = ""
    for i in range(1, num + 1):
        result += ' ' * (num - i) + '#' * i
        if i < num:
            result += '\n'
    return result

