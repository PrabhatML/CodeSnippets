# It is a comparison-based algorithm in which each 
# pair of adjacent elements is compared
# and the elements are swapped if they are not in order.

def bubble_sorter(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

    return list

if __name__ == '__main__':
    list = [12,2,34,9,23]
    b = bubble_sorter(list)
    print(b)