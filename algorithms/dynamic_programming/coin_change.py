def count(arr,m,n):
    table = [[0 for i in range(n+1)] for i in range(m)]
    print(table)

    for i in range(m):
        table[i][0] = 1


    for i in range(m):
        for j in range(n+1):
            if arr[i]>j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] + table[i][j-arr[i]]
            print(i,j,table)
    return table[m][n]


arr = [1,2,3]
m = len(arr)
n = 4
x = count(arr,m,n)
print(x)