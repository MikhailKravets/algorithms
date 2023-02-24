
def add_prefix_un(word: str) -> str:
    return "un" + word


def make_word_groups(vocab_words: list[str]) -> str:
    prefix = vocab_words[0]
    vocab_words = vocab_words[1:]

    # List Comprehension
    # result = []
    # for v in vocab_words:
    #     result.append(prefix + v)

    result = [prefix + v for v in vocab_words]

    # f-string
    return f"{prefix} :: " + " :: ".join(result)


def remove_suffix_ness(word: str) -> str:
    word = word.removesuffix("ness")
    if word.endswith("i"):
        word = word.removesuffix("i") + "y"
    return word


def adjective_to_verb(sentence: str, index: int) -> str:
    sentence = sentence.removesuffix(".")
    arr = sentence.split()
    adj = arr[index]

    return f"{adj}en"


if __name__ == '__main__':
    print(add_prefix_un('happy'))

    print()
    print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
    print(make_word_groups(['pre', 'serve', 'dispose', 'position']))

    print()
    print(remove_suffix_ness("heaviness"))
    print(remove_suffix_ness("sadness"))
    print(remove_suffix_ness("sadnessless"))

    print()
    print(adjective_to_verb('I need to make that bright.', -1))
    print(adjective_to_verb('It got dark as the sun set.', 2))
