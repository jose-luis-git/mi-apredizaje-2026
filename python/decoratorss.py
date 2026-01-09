from functools import wraps

users = ["alice", "ralph"]

def verify_user(func):
    @wraps(func)
    def wrapper(user):
        if user not in users:
            return "Denied Access"
        return func(user)
    return wrapper

def register_access(func):
    @wraps(func)
    def wrapper(user):
        print(f"User {user} attempted to log in")
        return func(user)
    return wrapper

@register_access
@verify_user
def access_secret(user):
    return f"Welcome {user}"

print(access_secret("alice"))
print(access_secret("bob"))