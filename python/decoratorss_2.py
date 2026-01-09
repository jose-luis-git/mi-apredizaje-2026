from functools import wraps
from time import perf_counter

person = "Marco"
person2 = ""

def check_user(func):
    @wraps(func)
    def wrapper(user):
        if not user:
            return "Unauthorized user"
        return func(user)
    return wrapper

def mesaure_time(func):
    @wraps(func)
    def wrapper(user):
        start = perf_counter()
        result = func(user)
        end = perf_counter()
        print(f"Execution time: {end - start:.6f}seconds")
        return(result)
    return wrapper

@mesaure_time
@check_user
def get_private_data(user):
    return f"Private data for {user}"

print(get_private_data("Marco"))
print(get_private_data(""))