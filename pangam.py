

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') == set(s.lower().replace(' ', ''))


def f(a=None):
    if not a:
        a = []
    a.append(3)
    return a


if __name__ == "__main__":
    n = [4, 5]
    b = f()
    c = f(n)
