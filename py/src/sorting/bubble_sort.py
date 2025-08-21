def bubble_sort(inp: list[int]) -> list[int]:
    len_inp = len(inp)
    for k in range(1, len_inp):
        swap = 0
        for i in range(len_inp - k):
            if inp[i] > inp[i + 1]:
                inp[i + 1], inp[i] = inp[i], inp[i + 1]
                swap += 1
        if not swap:
            break
    return inp
