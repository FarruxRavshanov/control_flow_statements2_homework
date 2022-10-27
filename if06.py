def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """

    a=n//10000
    b=(n//1000)%10
    c=(n//100)%10
    s=(n//10)%10
    q=(n%10)
    if a>b and a>c and a>s and a>q:
        d=5
    elif b>a and b>c and b>s and b>q:
        d=4
    elif c>a and c>b and c>s and c>q:
        d=3
    elif s>a and s>b and s>c and s>q:
        d=2
    elif q>a and q>b and q>c and q>s:
        d=1
    return d