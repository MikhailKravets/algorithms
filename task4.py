import typing
from numbers import Number


def replacer(s1: str, s2: str) -> str:
    two_s1, two_s2 = s1[:2], s2[:2]  # Collection Slice
    return f"{two_s2 + s1[2:]} {two_s1 + s2[2:]}"  # f-string


def add(a: float, b: float) -> float:
    if not isinstance(a, float) or not isinstance(b, float):
        raise TypeError("a or b should be float type")
    return a + b


def remove_duplicates(l: list[typing.Any]) -> list[typing.Any]:
    return list(set(l))


def has_same_element(l1: list[int], l2: list[int]) -> bool:
    for v1, v2 in zip(l1, l2):
        if v1 == v2:
            return True
    return False


def element_wise_sum(l1: list[int], l2: list[int]) -> list[int]:
    return [v1 + v2 for v1, v2 in zip(l1, l2)]  # List Comprehension


if __name__ == "__main__":
    print(replacer("H", "W"))

    collection = ["One", "Two", "Three"]
    print("; ".join(collection))

    print(add(4.0, 6.4))

    example = [4, 5, 6, 6, 6, 6]
    res = remove_duplicates(example)
    print(example)
    print(res)

    print(has_same_element(example, [5, 5, 6, 5, 6, 5]))
    print(element_wise_sum(example, [5, 5, 6, 5, 6, 5]))
