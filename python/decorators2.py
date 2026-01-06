from functools import wraps

while(True):
    try:
        name = input("Enter your name: ")
        if name.strip() == "":
            raise ValueError
        break
    except ValueError:
        print("Empty name")


def verificate_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Finished function")

        return result
    return wrapper

@verificate_user
def user(name):
    return name

print(f"The name user is: {user(name)}")