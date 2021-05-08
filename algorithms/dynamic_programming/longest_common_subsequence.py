
def print_t(table):
    for i in table:
        print(i)

def lcs(x,y):
    l1 = len(x)
    l2 = len(y)

    L = [[0 for i in range(l1+1)] for i in range(l2+1)]
    print_t(L)

    
    for i in range(l2+1):
        for j in range(l1+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif y[i-1]==x[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1],L[i-1][j])
    
    return(L[l2][l1])

# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is " + str(lcs(X, Y)))