#Create a function that takes two parameters, x and y, and swaps their values without using any additional variables. 
#The function should also check if both x and y are numeric values (integers or floats) before performing the swap. If either of the parameters is not numeric, the function should return an error message.
def swap(x, y):
    # Check if x and y are numeric
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return print(f"{-1}: Both x and y must be numeric values.")

    # Swap values using only x and y as variables
    x, y = y, x

    # Print the swapped values
    print(f"Swapped values: {x}, {y}")

# Example usage of the swap function
swap("Apple", 10)  # Output: Error: Both x and y must be numeric values.
swap(9, 17)  # Output: Swapped values: 17,9