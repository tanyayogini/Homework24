def filter_query(value, data):
    return filter(lambda x: value in x, data)


def map_query(value, data):
    column_number = int(value)
    return map(lambda x: x.split(' ')[column_number], data)


def unique_query(data, *args, **kwargs):
    return set(data)


def limit_query(value, data):
    limit = int(value)
    return list(data)[:limit]


def sort_query(value, data):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)
