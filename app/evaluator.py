def exact_match(actual: str, expected: str) -> bool:
    """
    Check whether the actual answer exactly matches the expected answer.
    """
    return actual.strip().lower() == expected.strip().lower()


def contains_expected(actual: str, expected: str) -> bool:
    """
    Check whether the expected answer is contained inside the actual answer.
    """
    return expected.strip().lower() in actual.strip().lower()