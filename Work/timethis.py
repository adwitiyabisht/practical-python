import time
from functools import wraps

def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"{func.__module__}.{func.__name__}: {execution_time:.6f} seconds")
        return result

    return wrapper