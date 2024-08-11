def filterEvenNumbers(numbers):
    """Filter out even numbers from a list of numbers."""
    return [num for num in numbers if num % 2 == 0]

print(filterEvenNumbers([0, -2, -4]))
    