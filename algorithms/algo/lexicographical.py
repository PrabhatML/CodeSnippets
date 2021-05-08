from itertools import permutations

def lexi_permu(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        print(x)
    

str = "abc"
lexi_permu(str)