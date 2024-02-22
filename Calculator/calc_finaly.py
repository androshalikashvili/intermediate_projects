# Check for number input
def check_input_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# function for add operation
def add(x, y):
    return x + y

# function for minus operation
def minus(x, y):
    return x - y

# function for multiply operation
def multiply(x, y):
    return x * y

# function for divide operation
def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Error: Do not divide by zero")


#recivie number
number_1 = input("Please input first number: ")
while not check_input_number(number_1):
    print("Error: Please input a valid number!")
    number_1 = input("Please input first number: ")

number_2 = input("Please input second number: ")
while not check_input_number(number_2):
    print("Error: Please input a valid number!")
    number_2 = input("Please input second number: ")

#Action selection check
while True:
    try:
        qmedeba = input("Please choose operation (+, -, *, /): ")

        if qmedeba == '+':
            res = add(float(number_1), float(number_2))
        elif qmedeba == '-':
            res = minus(float(number_1), float(number_2))
        elif qmedeba == '*':
            res = multiply(float(number_1), float(number_2))
        elif qmedeba == '/':
            res = divide(float(number_1), float(number_2))
        else:
            print("Error: Choose the right operation.")
            continue
        break

    except KeyboardInterrupt as ex:
        print("\nProgramm closed by user (Ctrl+C)")
        break

#produce results
print(f"Result: {number_1} {qmedeba} {number_2} = {res}")
