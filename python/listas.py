while(True):
    try:
        amount = int(input("Enter the number of numbers you will add: "))
        if amount <= 0:
            raise ValueError("Invalid amount")
        break
    except ValueError as e:
        print("Invalid amount enter a number")

notes = []


for i in range(amount):
    while(True):
        try:
            note = int(input("Enter your note: "))
            notes.append(note)
            break
        except ValueError:
            print("Enter a valid number")

def total_sum(*args):
    total = 0


    for number in args:
        total += number

    return total

def average(*args):
    if len(args) == 0:
        return 0
    return total_sum(*args) / len(args)


addition = total_sum(*notes)
averages = average(*notes)

print(f"The sum of the grades is: {addition}")
print(f"The average of the grades is: {averages}")