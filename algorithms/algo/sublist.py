def sublist(l):
    lists = [[]]
    for i in range(len(l)):
        orig = lists[:]
        new = [l[i]]
        for j in range(len(lists)):
            lists[j]  = lists[j] + new
        lists = orig + lists
    return lists
l1 = [1,2,3]
print(sublist(l1))