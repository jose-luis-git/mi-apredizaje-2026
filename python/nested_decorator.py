import time
from functools import wraps

def calculating_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start  = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Time: {end - start:.4f} seconds")
            
            return result
        return wrapper

def show_message(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function start")
        result = func(*args, **kwargs)
        print("finished function")

        return result
    return wrapper

@show_message
@calculating_time
def measure_time():
    total = 0


    for i in range(1_000_000):
        total += i

    return total

result = measure_time()
print("Result: ", result)