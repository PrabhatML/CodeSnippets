'''
Basic example of decorators
'''
import time

def deco(func):
    def inner():
        start = time.time()
        func()
        print("Execution time of "+func.__name__+"= "+str(time.time()-start))
    return inner

@deco
def ordinary():
    a = 0
    for i in range(1000000):
        a += i

ordinary()