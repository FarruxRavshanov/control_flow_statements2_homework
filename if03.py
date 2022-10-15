def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if b >= a >= c or c >= a >= b:
        md = a

    if a >= b >= c or c >= b >= a:
        md = b

    if a >= c >= b or b >= c >= a:
        md = c
    return md

print(main(5, 4, 5))