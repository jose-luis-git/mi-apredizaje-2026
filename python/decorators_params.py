from functools import wraps

while(True):
    try:
        amount = int(input("Enter de number the numbers you entered: "))
        if amount  <= 0:
            raise ValueError
        break
    except ValueError:
        print("Enter a valid number")

def repeat_numbers(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                print(f"Execution {i+1}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_numbers(amount)
def greet():
    print("Hello")

greet()