def get_integer_input() -> int:
    """
    Function to prompt the user to input an integer.
    This function keeps asking for input until a valid integer is provided.
    
    Returns:
        int: The integer input by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Function to check if the number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A formatted string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main function to drive the program. It calls get_integer_input and check_even_odd,
    and displays the result.
    """
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
