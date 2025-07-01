from typing import Callable
from time import perf_counter_ns as ns_timestamp
from time import sleep
from random import random

def timed(func: Callable[[], None]) -> Callable[[], int]:
    def inner_function():
        start_time = ns_timestamp()
        func()
        end_time = ns_timestamp()
        elapsed_time = (end_time - start_time)
        return elapsed_time
    
    return inner_function

called = 0

@timed
def f():
    global called
    called += 1
    sleep(random()) # sleep for a random amount of time

elapsed = f()
print(elapsed, 'ns elapsed')

assert called == 1

elapsed = f()
print(elapsed, 'ns elapsed')

assert called == 2