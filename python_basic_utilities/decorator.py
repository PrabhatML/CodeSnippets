
'''
Basic example of decorators
'''
import time

def deco_wapper_for_parameters(*args, **kwargs):
    def deco(func):
        def inner(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            print("Execution time of "+func.__name__+"= "+str(time.time()-start))
        return inner
    return deco

@deco_wapper_for_parameters(wait=5)
def ordinary(a=5):
    a = 0
    for i in range(1000000):
        a += i

ordinary()