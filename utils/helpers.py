import math


def make_chunks(iterable, group_number):
    """Split collection on equal groups"""
    part_len = math.ceil(len(iterable) / group_number)
    return [iterable[part_len * k:part_len * (k + 1)] for k in range(group_number)]


def make_date_chunks(iterable, group_number):
    """Split date range on equal groups"""
    start = min([p.order_date for p in iterable])
    end = max([p.order_date for p in iterable])
    diff = (end - start) / group_number
    res = []
    for i in range(group_number):
        res.append(start + diff * i)
    res.append(end)
    return res
