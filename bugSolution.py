def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

#This will not produce any error
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

#This will not produce any error
my_numbers = [10,20,30,40,50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")
