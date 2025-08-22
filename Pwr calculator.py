def calculate_power():
    """
    Calculates the power of a given number for n number of times.
    """
    try:
        base = float(input("Enter the base number: "))
        num_powers = int(input("Enter the number of powers to calculate (n): "))

        if num_powers < 1:
            print("Number of powers must be at least 1.")
            return

        print(f"\nCalculating powers of {base}:")
        for i in range(1, num_powers + 1):
            result = base ** i
            print(f"{base}^{i} = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Call the function to run the program
calculate_power()