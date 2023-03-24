from functions import filter_query, map_query, unique_query, limit_query, sort_query

CMD_TO_FUNCTION = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
}


def read_file(file_name):
    with open(file_name) as f:
        for line in f:
            yield line


def build_query(cmd, value, file_name, data):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    func = CMD_TO_FUNCTION[cmd]
    func_result = func(value=value, data=prepared_data)

    return list(func_result)
