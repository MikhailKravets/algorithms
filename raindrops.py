
def raindrops(number: int) -> str:
    s = ""
    if number % 3 == 0:
        s += "Pling"
    if number % 5 == 0:
        s += "Plang"
    if number % 7 == 0:
        s += "Plong"

    if s:
        return s
    return str(number)


if __name__ == '__main__':
    print(raindrops(28))
    print(raindrops(30))
    print(raindrops(34))
