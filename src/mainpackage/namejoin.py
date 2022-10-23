"""
This file just joins strings. It's very simple.
"""


def joinStrings(*strings: str, separator: str = ' ') -> str:
    """
    Join several strings into a single larger string.

    :param list[str] strings: The strings that will be joined.
    :param str separator: The separator that will separate the strings. Default is to use a space.
    :returns str: The result of joining these strings together
    """

    ret = ""
    for i in range(0, len(strings)):
        if i > 0:
            ret += separator
        ret += strings[i]
    return ret
