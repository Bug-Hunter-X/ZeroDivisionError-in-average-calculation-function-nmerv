def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (this will produce a ZeroDivisionError)
average = calculate_average([])