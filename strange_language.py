

VOWELS = "aeiou"


def translate(word: str) -> str:
    prefix = word[:2]
    if prefix == 'xr' or prefix == 'yt' or word[0] in VOWELS:
        return f"{word}ay"

    prefix = ""
    yprefix = ""
    for v in word:
        if v not in VOWELS:
            prefix += v
        else:
            break
        if v == "y":
            yprefix = prefix[:-1]

    if yprefix and word[len(yprefix)] == "y":
        return f"y{word.replace(yprefix + 'y', '')}{yprefix}ay"
    if prefix[-1] == "q" and word[len(prefix)] == "u":
        prefix += "u"

    return f"{word.replace(prefix, '')}{prefix}ay"


if __name__ == '__main__':
    print(translate("apple"))
    print(translate("xrapple"))
    print(translate("chair"))
    print(translate("square"))
    print(translate("rhythm"))

