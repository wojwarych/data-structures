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


def _merge(l: list[int]):
    if len(l) <= 1:
        return l

    start = 0
    end = len(l)
    mid = (end - start) // 2

    sub_1 = _merge(l[start:mid])
    sub_2 = _merge(l[mid:end])
    return _combine(sub_1, sub_2)

def merge_sort(inp: list[int]) -> list[int]:
    return _merge(inp)
