from typing import Callable
from time import perf_counter_ns as ns_timestamp
from time import sleep
from random import random

def worst_case_timed(func: Callable[[], None]) -> Callable[[], int]:
    maxRet: int = 0
    def inner_function():
        nonlocal maxRet
        start = ns_timestamp()
        func()
        end = ns_timestamp()
        elapsed_time = end-start
        maxRet = max(maxRet, elapsed_time)
        return maxRet
    return inner_function

called = 0

@worst_case_timed
def f():
    global called
    called += 1
    sleep(random()) # sleep for a random amount of time

worst_elapsed = f()
print(worst_elapsed, 'ns elapsed so far in the worst case')

assert called == 1

worst_elapsed = f()
print(worst_elapsed, 'ns elapsed so far in the worst case')

assert called == 2

worst_elapsed = f()
print(worst_elapsed, 'ns elapsed so far in the worst case')

assert called == 3