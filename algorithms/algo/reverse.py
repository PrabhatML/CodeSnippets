def reverse(str):
    l = len(str)
    out = ""

    for i in range(l):
        out += str[l-i-1]

    return out


str = "prabhat"
print(reverse(str))