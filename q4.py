def string_reverse(s):
    """Reverses a given string after validating it is a string."""
    if not isinstance(s, str):
        return "Error: Input must be a string"
    return s[::-1]


# Task 2: Invoke the function with test scenarios
print("Original String: Hello World")
print(f"Reversed String: {string_reverse('Hello World')}\n")
print("Original String: Python")
print(f"Reversed String: {string_reverse('Python')}")
