def occurenceofnumber(lst,n):
    if n not in lst:
        return 0
    hmap = {}
    for i in lst:
        if i not in hmap.keys():
            hmap[i] = 1
        else:
            hmap[i] += 1
    return hmap[n]




a = [0,5,5,5,6]
n = 4
print(occurenceofnumber(a,n))