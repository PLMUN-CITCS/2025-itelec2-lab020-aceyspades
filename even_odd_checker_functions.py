def get_integer():
    number = input("Enter an integer: ")
    try:
        number = int(number)
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_integer()

def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    number = get_integer()
    result = check_even_or_odd(number)
    print(result)

if __name__ == "__main__":
    main()
