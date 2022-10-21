def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    max = 0
    x1 = n % 10
    max = x1
    
    x2 = n // 10 % 10
    if x2 > x1:
        max = x2

    x3 = n // 100 % 10
    if x3 > x2:
        max = x3

    x4 = n // 1000 % 10
    if x4 > x3:
        max = x4

    x5 = n // 10000
    if x5 > x4:
        max = x5
    
    
    return max

print(main(98765))