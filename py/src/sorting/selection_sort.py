import random


def selection_sort(inp: list[int]) -> list[int]:
    for i, _ in enumerate(inp):
        min_ = i
        for j in range(i+1, len(inp)):
            if inp[j] < inp[min_]:
                min_ = j
        inp[i], inp[min_] = inp[min_], inp[i]
    return inp


if __name__ == "__main__":
    R = range(1000)
    r = [random.choice(R) for _ in range(1000)]
    print(selection_sort(r))
