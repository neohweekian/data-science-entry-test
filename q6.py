"""This code defines a function `find_first_negative` that takes a list of numbers as input and 
returns the first negative number found in the list. If there are no negative numbers, 
it returns the string "No negatives". 
The function uses a while loop to iterate through the list and check each element for negativity.
"""
def find_first_negative(lst):
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    return "No negatives"


# Scenario 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(f"Scenario 1: {result1}")

# Scenario 2
result2 = find_first_negative([2, 10, 7, 0])
print(f"Scenario 2: {result2}")