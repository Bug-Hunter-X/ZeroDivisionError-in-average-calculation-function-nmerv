def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (this will now return 0)
average = calculate_average([]) 
print(average) # Output: 0

#Example with numbers
average = calculate_average([10,20,30])
print(average) #Output: 20.0