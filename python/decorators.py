while(True):
    try:
        amount = int(input("Enter the number of numbers you will add: "))
        if amount <= 0:
            raise ValueError
        break
    except ValueError:
        print("Enter a valid amount")

numbers = []

for i in range(amount):
    while(True):
        try:
            number = int(input("Enter a number: "))
            numbers.append(number)
            break
        except ValueError:
            print("Enter a valid number")

def validate_positive(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        for n in args:
            if n < 0:
                raise ValueError("Only positive numbers are allowed")
            
        result = func(*args, **kwargs)

        print("After function")
        
        return result 
    return wrapper

@validate_positive
def add(*numbers):
    return numbers
try:
    print(f"The list is: {add(*numbers)}")
except ValueError as e:
    print(f"Error: {e}")
            