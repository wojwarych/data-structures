import random


def bubble_sort(input_list: list[int]) -> list[int]:
    for i in range(1, len(input_list)):
        swap = 0
        for j in range(len(input_list) - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1]
                swap += 1
        if not swap:
            break
    return input_list


R = range(100)
r = [random.choice(R) for _ in range(10)]
print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

