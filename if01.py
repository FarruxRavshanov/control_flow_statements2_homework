def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mx = a
    if a < b:
        mx = b

    if a < c:
        mx = c

    return mx

print(main(3, 5, 1))