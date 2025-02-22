def get_integer():
    """
    This function prompts the user to enter an integer and ensures that the input is valid.
    It handles invalid inputs and keeps asking until a valid integer is entered.
    """
    number = input("Enter an integer: ")
    try:
        number = int(number)
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_integer()

def check_even_or_odd(number):
    """
    This function checks if the given number is even or odd.
    It returns a formatted string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def display_result(result):
    """
    This function displays the result of the even/odd check.
    It takes in the result as a string and prints it.
    """
    print(result)

def main():
    """
    Main function to drive the program.
    - Calls get_integer() to retrieve a valid integer from the user.
    - Checks whether the number is even or odd.
    - Displays the result.
    """
    number = get_integer()
    result = check_even_or_odd(number)
    display_result(result)

if __name__ == "__main__":
    main()
