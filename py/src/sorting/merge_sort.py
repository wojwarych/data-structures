def _combine(sub_1: list[int], sub_2: list[int]):
    ret = []
    while sub_1 and sub_2:
        if sub_1[0] < sub_2[0]:
            ret.append(sub_1.pop(0))
        else:
            ret.append(sub_2.pop(0))

    if sub_1:
        for el in sub_1:
            ret.append(el)

    if sub_2:
        for el in sub_2:
            ret.append(el)

    return ret


def _merge(a_list: list[int]):
    if len(a_list) <= 1:
        return a_list

    start = 0
    end = len(a_list)
    mid = (end - start) // 2

    sub_1 = _merge(a_list[start:mid])
    sub_2 = _merge(a_list[mid:end])
    return _combine(sub_1, sub_2)


def merge_sort(inp: list[int]) -> list[int]:
    return _merge(inp)
