from typing import Iterable, Any, Iterator
import re


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    column_number: int = int(value)
    return map(lambda x: x.split(' ')[column_number], data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set[str]:
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> list[str]:
    limit: int = int(value)
    return list(data)[:limit]


def sort_query(value: str, data: Iterable[str]) -> list[str]:
    reverse: bool = value == 'desc'
    return sorted(data, reverse=reverse)


def regexp_query(value: str, data: Iterable[str]) -> Iterator[str]:
    regexp = re.compile(value)
    return filter(lambda x: re.search(regexp, x), data)

