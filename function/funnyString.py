def funnyString(s):
    r = "".join(reversed(s))
    re_ascii = [ord(i) for i in r]
    ascii = [ord(i) for i in s]
    for i in range(1, len(s)):
        if abs(ascii[i] - ascii[i - 1]) != abs(re_ascii[i] - re_ascii[i - 1]):
            return "Not Funny"
    return "Funny"
