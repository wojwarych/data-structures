def insertion_sort(input_list: list[int]) -> list[int]:
    for i in range(1, len(input_list)):
        val = input_list[i]
        j = i - 1
        while j > -1 and input_list[j] > val:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = val

    return input_list
