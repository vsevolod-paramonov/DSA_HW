

def max_divisor(number: int):

    div = 1
    while number // div >= 10:
        div *= 10

    return div


def is_palindrome(number: int):

    if number < 0:
        return False
 
    l, r = max_divisor(number), 10

    while number > 0:
        if number // l != number % r:
            return False

        number = (number % l) // r
        l //= 100

    return True
