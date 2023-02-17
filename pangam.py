

def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') == set(s.lower().replace(' ', ''))


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
