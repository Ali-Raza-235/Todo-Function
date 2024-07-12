def menu():
    options = """
    Perform all type of Calculations in one line, Press 'all'
    For Addition, Press 'a'
    For Subtraction, Press 's'
    For Division, Press 'd'
    For Multiplication, Press 'm'
    For Quit, Press 'q'
    """

    choose_option = input(options).lower()

    while choose_option != 'q':
        if choose_option == 'all':
            all()
        elif choose_option == 'a':
            addition()
        elif choose_option == 's':
            subtraction()
        elif choose_option == 'd':
            division()
        elif choose_option == 'm':
            multiplication()
        else:
            print("Invalid Input, Please Try Again!")

        choose_option = input(options).lower()

def all():
    expression = input('Enter your Expression to perform calculation: ')
    try:
        print(eval(expression))
    except Exception as e:
        print(f"Error in evaluating expression: {e}")

def addition():
    number1 = int(input('Enter Your First Number: '))
    number2 = int(input('Enter Your Second Number: '))

    print(number1 + number2)

def subtraction():
    number1 = int(input('Enter Your First Number: '))
    number2 = int(input('Enter Your Second Number: '))

    print(number1 - number2)

def division():
    number1 = int(input('Enter Your First Number: '))
    number2 = int(input('Enter Your Second Number: '))

    print(number1 / number2)

def multiplication():
    number1 = int(input('Enter Your First Number: '))
    number2 = int(input('Enter Your Second Number: '))

    print(number1 * number2)

menu()
