from functools import wraps

logged_in = False

def max_call(maximo):
    def decorator(func):
        call = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call

            if call >= maximo:
                print("Limit reached")
                return
            call += 1
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Access denied")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
@max_call(3)
def pay():
    print("Login OK")


for i in range(5):
    pay()

print("\n"*6)

logged_in = True

for i in range(5):
    pay()