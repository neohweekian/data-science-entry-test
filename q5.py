def check_divisibility(num, divisor):
    """
    Check if num is divisible by divisor.
    Both num and divisor must be numeric.
    Returns True if divisible, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False
    if divisor == 0:
        return False
    return num % divisor == 0


# Scenario 1: num=10, divisor=2
result1 = check_divisibility(10, 0)
print(f"check_divisibility(10, 0) = {result1}\n")

# Scenario 2: num=7, divisor=3
result2 = check_divisibility(7, 3)
print(f"check_divisibility(7, 3) = {result2}")