def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if temp <= 0:
        d = 'Freezing'

    if 1 <= temp <= 10:
        d = 'Very Cold'

    if 11 <= temp <= 20:
        d = 'Cold'

    if 21 <= temp <= 30:
        d = 'Normal'

    if 31 <= temp <= 40:
        d = 'Hot'

    if temp >= 40:
        d = 'Very Hot'
    return d

print(main(23))