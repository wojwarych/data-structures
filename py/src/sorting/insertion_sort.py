import random


def insertion_sort(inp: list[int]) -> list[int]:
    len_inp = len(inp)
    for i in range(1, len_inp):
        j = i - 1
        val = inp[i]
        while j > -1 and inp[j] > val:
            inp[j + 1] = inp[j]
            j -= 1
        inp[j + 1] = val
    return inp




if __name__ == "__main__":
    R = range(100)
    r = [random.choice(R) for _ in range(5000)]
    print(insertion_sort(r))
