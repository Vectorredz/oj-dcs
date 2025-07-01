from typing import Callable, ParamSpec
import time

import functools
import time

def retry(n=3):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            attempts = 0
            while attempts < n:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= n:
                        raise
                    time.sleep(1)  # Optional: wait 1 second before retrying
        return wrapper_retry
    return decorator_retry

# Example usage
@retry(n=2)
def test_function():
    print("Trying...")
    raise ValueError("An error occurred")

try:
    test_function()
except ValueError as e:
    print(e)

      

# def log_time(f: Callable[[], None]):
#     def inner_function():
#         start_time = perf_counter_ns()
#         end_time = perf_counter_ns()
#         elapsed_time = end_time - start_time
#         print(f"{f.__name__}: {elapsed_time} ns")
#     return inner_function


# @log_time
# def log_into_crs():
#     ...

# log_into_crs()

# @log_time
# def go_to_curriculum_checklist_page():
#     ...

# go_to_curriculum_checklist_page()

# @log_time
# def download_curriculum_checklist():
#     ...

# download_curriculum_checklist()
