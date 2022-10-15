def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mn = a
    if a > b:
        mn = b

    if a > c:
        mn = c

    return mn

print(main(3, 5, 1))