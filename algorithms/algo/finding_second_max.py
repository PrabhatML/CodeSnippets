list1 = [10,20,3,45,99]

mx = max(list1[0],list1[1])
second_mx = min(list1[0],list1[1])
l = len(list1)
for i in range(2,l):
    if list1[i] > mx:
        second_mx = mx
        mx = list1[i]
    elif list1[i] > second_mx and mx != list1[i]:
        second_mx = list1[i]

print(second_mx)