MAX = 100

def calculate_sum(arr):
    """Calculate the sum of a list of numbers."""
    return sum(arr)

def get_number_of_elements():
    """Prompt the user to enter the number of elements and validate the input."""
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX}): "))
            if 1 <= n <= MAX:
                return n
            else:
                print(f"Invalid input. Please enter a number between 1 and {MAX}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompt the user to enter n integers and validate the input."""
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                num = int(input())
                arr.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return arr

def main():
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()