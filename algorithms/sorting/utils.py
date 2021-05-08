import time

def execution_time(func):
    def inner(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        total = time.time() - t
        print(f'Execution time of function {func.__name__} is {total}')
        return result
    return inner

if __name__ == "__main__":
    pass