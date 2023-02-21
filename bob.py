
def bob(question: str) -> str:
    if question == "what's up?":
        return "Sure"
    if question.isupper() and question.endswith("?"):
        return "Relax, I know what I'm doing"
    if question.isupper():
        return "Wow relax"
    if question == "":
        return "OK, be so"
    return "Whatever"


def bbb():
    "fhrefeuuy"


if __name__ == '__main__':
    res = bob("......")
    print(res)
