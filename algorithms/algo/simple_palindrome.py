def ispalindrome(str):
    l = len(str)
    for i in range(0,int(l/2)):
        if str[i] != str[l-i-1]:
            return False
    return True
    