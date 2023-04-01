from typing import Iterable, Optional, Callable

from functions import filter_query, map_query, unique_query, limit_query, sort_query, regexp_query

CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regexp_query,
}


def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as f:
        for line in f:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> list[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    func = CMD_TO_FUNCTION[cmd]
    func_result = func(value=value, data=prepared_data)

    return list(func_result)
