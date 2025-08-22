"""Implementation of Radix Sort for LSD (Least Significant Digit)"""


def radix_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    radix_arr: list[list[int]] = [[], [], [], [], [], [], [], [], [], []]
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        while len(arr) > 0:
            val = arr.pop()
            digit = (val // exp) % 10
            radix_arr[digit].append(val)

        for radix in radix_arr:
            while len(radix) > 0:
                arr.append(radix.pop())

        exp *= 10

    return arr
