def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
print("Select operation.")
print("1. Add")
print("2")

while True:
    choice = input("Enter choice (1/2/3/4):")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        expect ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif

        next_calculation = input("Let's do next calcluation? (y/n):")
        if next_cal == "no":
            break
    else:
        print("Invalid Input")
