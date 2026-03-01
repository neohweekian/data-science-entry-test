def update_dictionary(dct, key, value):
    """
    Updates dictionary with a new key-value pair.
    If the key already exists, prints the original value before updating.
    Returns the updated dictionary.
    """
    if key in dct:
        print(f"{key} already exists. Original value: {dct[key]}")
    dct[key] = value
    return dct


# Scenario 1: Empty dictionary with new key
print("Scenario 1:")
result1 = update_dictionary({}, "name", "Alice")
print(f"Updated dictionary: {result1}\n")

# Scenario 2: Dictionary with existing key
print("Scenario 2:")
result2 = update_dictionary({"age": 25}, "age", 26)
print(f"Updated dictionary: {result2}")
