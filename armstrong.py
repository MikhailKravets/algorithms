

def is_armstrong(number: int) -> bool:
    digits = []  # [3, 5, 1]

    n = number
    while n != 0:
        digits.append(n % 10)
        n //= 10

    new_number = 0
    l = len(digits)
    for v in digits:
        new_number += v ** l

    return number == new_number


if __name__ == '__main__':
    print(is_armstrong(153))
