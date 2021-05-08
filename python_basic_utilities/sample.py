
'''
Basic example of decorators
'''
import time

def deco_wapper_for_parameters(*args, **kwargs):
    print(args,kwargs)
    def deco(func):
        print(func.__name__)
        def inner(*args, **kwargs):
            print(args,kwargs)
            start = time.time()
            func(*args, **kwargs)
            print("Execution time of "+func.__name__+"= "+str(time.time()-start))
        return inner
    return deco

@deco_wapper_for_parameters(wait=5)
def ordinary(a=5):
    print(a)
    a = 0
    print(a)
    for i in range(1000000):
        a += i

ordinary()