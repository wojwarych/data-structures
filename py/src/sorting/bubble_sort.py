def bubble_sort(input_list: list[int]) -> list[int]:
    list_length = len(input_list)

    for i in range(1, list_length):
        swap = 0
        for j in range(list_length - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1]
                swap += 1
        if not swap:
            break
    return input_list
