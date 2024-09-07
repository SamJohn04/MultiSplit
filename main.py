from typing import Callable, Iterable


def multisplit(string: str, delims: list[str], keep_delims: bool = False, keep_empty: bool = False):
    strings = [string]
    for delim in delims:
        strings = flatmap(strings, lambda string: split(string, delim, keep_delims, keep_empty))
    return strings


def split(string: str, delim: str, keep_delims: bool = False, keep_empty: bool = False):
    result = string.split(delim)
    if keep_delims:
        result = flatmap(enumerate(result), lambda item: [item[1], delim] if item[0] < len(result) - 1 else [item[1]])
    if not keep_empty:
        result = list(filter(lambda item: item != '', result))
    return result


def flatmap(initial_iter: Iterable, predicate: Callable) -> list:
    result = []
    for item in initial_iter:
        result.extend(predicate(item))
    return result

