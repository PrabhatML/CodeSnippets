import time
import threading

start = time.perf_counter()

def do_something(seconds = 1):
    print(f"Sleeping {} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping...")

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')