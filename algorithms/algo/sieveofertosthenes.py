def sieveofertosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p < n:
        if (prime[p] == True):
            for i in range(p*p, n+1,p):
                print(i)
                prime[i] = False
        p += 1
    
    for i in range(2,n+1):
        if prime[i]:
            print(i)






n = 50
sieveofertosthenes(n)